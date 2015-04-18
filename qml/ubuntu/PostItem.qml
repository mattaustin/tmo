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


ListItem.Empty {

    id: item

    property var post

    height: column.height + (2 * item.__contentsMargins)

    Column {

        id: column

        anchors {
            margins: item.__contentsMargins
            top: parent.top
            left: parent.left
            right: parent.right
        }

        Item {

            height: member.height + item.__contentsMargins
            width: parent.width

            Label {
                id: member
                anchors {
                    top: parent.top
                    left: parent.left
                }
                color: Theme.palette.normal.backgroundText
                fontSize: 'x-small'
                text: post.member
                wrapMode: Text.Wrap
            }

            Label {
                id: datetime
                anchors {
                    top: parent.top
                    right: parent.right
                }
                color: Theme.palette.normal.backgroundText
                fontSize: 'x-small'
                text: Qt.formatDateTime(post.datetime)
                wrapMode: Text.Wrap
            }

        }

        Label {
            id: content
            fontSize: 'small'
            text: post.content
            width: parent.width
            wrapMode: Text.Wrap
        }

    }

}
