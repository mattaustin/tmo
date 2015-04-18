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

    property var thread

    Component.onCompleted: {
        postList.appendItems();
    }

    BusyIndicator {
        id: busyindicator
        anchors.centerIn: parent
        running: client.busy //&& !postList.count
        size: BusyIndicatorSize.Large
    }

    SilicaListView {

        id: postList

        property int pageNumber: 1
        property bool hasNextPage: false

        anchors.fill: parent
        model: ListModel {}

        header: PageHeader {
            title: thread.title
        }

        delegate: Item {

            id: item
            height: contentItem.height + contextMenu.height
            width: postList.width

            PostItem {

                id: contentItem
                post: model

                onPressAndHold: {
                    contextMenu.show(item);
                }

            }

            ContextMenu {
                id: contextMenu
                MenuItem {
                    text: 'Copy url'
                    onClicked: {
                        Clipboard.text = model.url;
                        contextMenu.hide();
                    }
                }
                MenuItem {
                    text: 'Open website'
                    onClicked: {
                        Qt.openUrlExternally(model.url);
                        contextMenu.hide();
                    }
                }
            }

        }

        PullDownMenu {
            id: pullDownMenu
            MenuItem {
                text: 'Copy url'
                onClicked: {Clipboard.text = thread.url;}
            }
            MenuItem {
                text: 'Open website'
                onClicked: {Qt.openUrlExternally(thread.url);}
            }
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

        VerticalScrollDecorator {}

    }

}
