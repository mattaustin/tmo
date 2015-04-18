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
import Ubuntu.Components 0.1
import Ubuntu.Components.Popups 0.1


MainView {

    id: application

    width: units.gu(48)
    height: units.gu(60)
    useDeprecatedToolbar: false

    PageStack {

        id: pageStack

        Component.onCompleted: {
            // Theme.name = 'Ubuntu.Components.Themes.SuruGradient'
            push(Qt.resolvedUrl('ForumListPage.qml'))
        }

    }

    Client {
        id: client
    }

    Component {
        id: errorDialog
        ErrorDialog {}
    }

    function showError(message) {
        PopupUtils.open(errorDialog, null, {'message': message});
    }

}
