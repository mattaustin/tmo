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
import Sailfish.Silica 1.0


Page {

    Component.onCompleted: {
        client.getForums(function (result) {
            result.forEach(function (item) {
                forumList.model.append(item);
            });
        });
    }

    BusyIndicator {
        id: busyindicator
        anchors.centerIn: parent
        running: client.busy && !forumList.count
        size: BusyIndicatorSize.Large
    }

    SilicaListView {

        id: forumList
        anchors.fill: parent
        model: ListModel {}

        header: PageHeader {
            title: 'talk.maemo.org'
        }

        delegate: BackgroundItem {

            id: item
            width: forumList.width
            height: Theme.itemSizeSmall

            Item {

                x: Theme.paddingLarge
                anchors.verticalCenter: parent.verticalCenter
                width: parent.width - (2 * Theme.paddingLarge)

                Label {
                    text: model.name
                    color: item.down ? Theme.highlightColor : Theme.primaryColor
                    truncationMode: TruncationMode.Fade
                    anchors {
                        left: parent.left
                        right: parent.right
                        verticalCenter: parent.verticalCenter
                    }
                }

            }

            onClicked: {
                pageStack.push(Qt.resolvedUrl('ThreadListPage.qml'), {'forum': model})
            }

        }

        PullDownMenu {
            id: pullDownMenu
            MenuItem {
                text: 'About'
                onClicked: {
                    pullDownMenu.close();
                    pageStack.push(Qt.resolvedUrl('AboutDialog.qml'))
                }
            }
            MenuItem {
                text: 'Project homepage'
                onClicked: {Qt.openUrlExternally(client.projectUrl)}
            }
        }

        VerticalScrollDecorator {}

    }

}
