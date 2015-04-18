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

    property var forum

    Component.onCompleted: {
        threadList.appendItems();
    }

    BusyIndicator {
        id: busyindicator
        anchors.centerIn: parent
        running: client.busy //&& !threadList.count
        size: BusyIndicatorSize.Large
    }

    SilicaListView {

        id: threadList

        property int pageNumber: 1
        property bool hasNextPage: false

        anchors.fill: parent
        model: ListModel {}

        header: PageHeader {
            title: forum.name
        }

        delegate: BackgroundItem {

            id: backgroundItem
            height: item.height
            width: threadList.width

            Item {

                id: item

                width: parent.width - (2 * Theme.paddingLarge)
                height: childrenRect.height + (2 * Theme.paddingLarge)
                x: Theme.paddingLarge
                y: Theme.paddingLarge

                Label {
                    text: model.title
                    color: backgroundItem.down ? Theme.highlightColor : Theme.primaryColor
                    font.pixelSize: Theme.fontSizeSmall
                    truncationMode: TruncationMode.Fade
                    width: parent.width
                    wrapMode: Text.Wrap
                    maximumLineCount: 2
                }

            }

            onClicked: {
                pageStack.push(Qt.resolvedUrl('PostListPage.qml'), {'thread': model});
            }

        }

        PullDownMenu {
            id: pullDownMenu
            MenuItem {
                text: 'Copy url'
                onClicked: {Clipboard.text = forum.url;}
            }
            MenuItem {
                text: 'Open website'
                onClicked: {Qt.openUrlExternally(forum.url);}
            }
        }

        onAtYEndChanged: {
            if (atYEnd && count && hasNextPage && !client.busy) {
                pageNumber += 1
                appendItems();
            }
        }

        function appendItems() {
            client.getThreads(forum.url, pageNumber, function (result) {
                result[0].forEach(function (item) {
                    model.append(item);
                });
                hasNextPage = result[1];
            });
        }

        VerticalScrollDecorator {}

    }

}
