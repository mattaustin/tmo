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

    property var thread

    title: thread.title

    Component.onCompleted: {
        postList.appendItems();
    }

    ActivityIndicator {
        id: busyindicator
        anchors.centerIn: parent
        running: client.busy //&& !postList.count
    }

    ListView {

        id: postList

        property int pageNumber: 1
        property bool hasNextPage: false

        anchors.fill: parent
        model: ListModel {}

        delegate: PostItem {
            post: model
        }

        onAtYEndChanged: {
            if (atYEnd && count && hasNextPage && !client.busy) {
                pageNumber += 1
                appendItems();
            }
        }

        function appendItems() {
            client.getPosts(thread.url, pageNumber, function (result) {
                result[0].forEach(function (item) {
                    model.append(item);
                });
                hasNextPage = result[1];
            });
        }

        Scrollbar {
            flickableItem: parent
        }

    }

}
