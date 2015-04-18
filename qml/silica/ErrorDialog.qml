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

    id: dialog

    property string message: ''

    forwardNavigation: false

    SilicaFlickable {

        anchors.fill: parent
        contentHeight: column.height
        contentWidth: parent.width

        Column {

            id: column

            width: dialog.width
            spacing: Theme.paddingLarge

            PageHeader {
                title: 'Error'
            }

            Label {
                text: message
                color: Theme.highlightColor
                width: parent.width - (2 * Theme.paddingLarge)
                x: Theme.paddingLarge
                wrapMode: Text.WordWrap
                font.pixelSize: Theme.fontSizeSmall
            }

        }

    }

}
