// Copyright 2015 Matt Austin

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//     http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

import QtQuick 2.0
import io.thp.pyotherside 1.2


Python {

    property int busy: 0
    property bool logged_in: false
    property string projectUrl: ''
    property string version: ''

    Component.onCompleted: {
        addImportPath(Qt.resolvedUrl('../..'));
        addImportPath(Qt.resolvedUrl('..'));
        setMetaData();
    }

    onError: {
        console.log('Python error: ' + traceback);
        application.showError(traceback);
    }

    function login(username, password, callback) {
        busy += +1;
        importModule('tmo.qml', function() {
            call('tmo.qml.client.login', [username, password], function() {
                busy += -1;
                logged_in = true;
                typeof callback === 'function' && callback();
            });
         });
    }

    function logout(callback) {
        busy += +1;
        importModule('tmo.qml', function() {
            call('tmo.qml.client.logout', [], function() {
                busy += -1;
                logged_in = false;
                typeof callback === 'function' && callback();
            });
        });
    }

    function getForums(callback) {
        busy += +1;
        importModule('tmo.qml', function() {
            call('tmo.qml.get_forums', [], function(result) {
                busy += -1;
                typeof callback === 'function' && callback(result);
            });
        });
    }

    function getThreads(forum_url, page, callback) {
        busy += +1;
        importModule('tmo.qml', function() {
            call('tmo.qml.get_threads', [forum_url, page], function(result) {
                busy += -1;
                typeof callback === 'function' && callback(result);
            });
        });
    }

    function getPosts(thread_url, page, callback) {
        busy += +1;
        importModule('tmo.qml', function() {
            call('tmo.qml.get_posts', [thread_url, page], function(result) {
                busy += -1;
                typeof callback === 'function' && callback(result);
            });
        });
    }

    function setMetaData() {
        importModule('tmo', function () {
            projectUrl = evaluate('tmo.__url__');
            version = evaluate('tmo.__version__');
        });
    }

}
