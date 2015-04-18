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
import Ubuntu.Components.ListItems 0.1 as ListItem


Page {

    title: 'talk.maemo.org'

    Component.onCompleted: {
        client.getForums(function (result) {
            result.forEach(function (item) {
                forumList.model.append(item);
            });
        });
    }

    ActivityIndicator {
        id: busyindicator
        anchors.centerIn: parent
        running: client.busy && !forumList.count
    }

    ListView {

        id: forumList
        anchors.fill: parent
        model: ListModel {}

        delegate: ListItem.Standard {
            width: parent.width
            text: model.name
            onClicked: {
                pageStack.push(Qt.resolvedUrl('ThreadListPage.qml'), {'forum': model})
            }
        }

        Scrollbar {
            flickableItem: parent
        }

    }

}
