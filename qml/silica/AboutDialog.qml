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
                title: 'About'
            }

            Label {
                text: 'tmo v' + client.version
                color: Theme.highlightColor
                width: parent.width - (2 * Theme.paddingLarge)
                x: Theme.paddingLarge
                wrapMode: Text.WordWrap
                font.family: Theme.fontFamilyHeading
                font.pixelSize: Theme.fontSizeMedium
            }

            Label {
                text: 'Copyright (c) 2015 Matt Austin.\n\n\'tmo\' is free sofware licenced under the Apache License, Version 2.0.\n\nData is provided on an \"as is\" and \"as available\" basis. No representations or warranties of any kind, express or implied are made. This program accesses data using your internet connection. Your operator may charge you for data use.'
                color: Theme.highlightColor
                width: parent.width - (2 * Theme.paddingLarge)
                x: Theme.paddingLarge
                wrapMode: Text.WordWrap
                font.pixelSize: Theme.fontSizeExtraSmall
            }

        }

    }

}
