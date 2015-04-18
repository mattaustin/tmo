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


BackgroundItem {

    id: item

    property var post

    height: column.height
    width: parent.width

    Column {

        id: column


        width: parent.width - (2 * Theme.paddingLarge)
        height: childrenRect.height + (2 * Theme.paddingLarge)
        x: Theme.paddingLarge
        y: Theme.paddingLarge

        Item {

            height: member.height + Theme.paddingSmall
            width: parent.width

            Label {
                id: member
                anchors {
                    top: parent.top
                    left: parent.left
                }
                color: Theme.secondaryColor
                font.pixelSize: Theme.fontSizeExtraSmall
                text: post.member
                wrapMode: Text.Wrap
            }

            Label {
                id: datetime
                anchors {
                    top: parent.top
                    right: parent.right
                }
                color: Theme.secondaryColor
                font.pixelSize: Theme.fontSizeExtraSmall
                text: Qt.formatDateTime(post.datetime)
                wrapMode: Text.Wrap
            }

        }

        Label {
            id: content
            color: Theme.primaryColor
            font.pixelSize: Theme.fontSizeSmall
            text: post.content
            width: parent.width
            wrapMode: Text.Wrap
        }

    }

}
