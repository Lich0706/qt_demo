// import QtQuick.Controls
import QtQuick.Window
import QtLocation 5.6
import QtPositioning 6.5

Window {
    id: root
    width: 1280
    height: 720
    visible: true
    title: qsTr("Tesla Infotainment")
    
    // Connections {
    //     target: systemHandler
    //     function onCarLockedChanged(boolValue) {
    //         return
    //     }
    // }

    Rectangle {
        id: bottomBar
        anchors {
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }
        color: "black"
        height: parent.height / 12

        Image {
            id: carSettingIcon
            anchors {
                left: parent.left
                leftMargin: 30
                verticalCenter: parent.verticalCenter
            }
            height: parent.height * 0.85
            source: "asset/icon_car.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    Rectangle {
        id: rightScreen
        anchors {
            top: parent.top
            bottom: bottomBar.top
            right: parent.right
        }
        width: parent.width * 2/3
        Plugin {
            id: mapPlugin
            name: "osm"
            PluginParameter {
                name: "osm.mapping.providersrepository.disabled"
                value: "true"
            }
            PluginParameter {
                name: "osm.mapping.providersrepository.address"
                value: "http://maps-redirect.qt.io/osm/5.6/"
            }
        }
        Map {
            id: map
            anchors.fill: parent
            plugin: mapPlugin
            center: QtPositioning.coordinate(37.46, -122.14)
            zoomLevel: 14
        }

        Rectangle {
            id: navSearchBar
            color: "#f0f0f0"

            anchors {
                top: lockIcon.bottom
                left: lockIcon.left
                topMargin: 15
            }

            width: parent.width * 1/3
            height: parent.height * 1/12

            Image {
                id: searchIcon

                anchors {
                    left: parent.left
                    leftMargin: 15
                    verticalCenter: parent.verticalCenter
                }

                source: "asset/search.png"

                height: parent.height * .45
                fillMode: Image.PreserveAspectFit
            }

            Text {
            id: navPlaceHolderText
            visible: navTextInput.text === ""
            color: "#000000"
            text: "Navigate"
            anchors {
                verticalCenter: parent.verticalCenter
                left: searchIcon.right
                leftMargin: 20
                }
            }

            TextInput {
                id: navTextInput
                clip: true
                anchors {
                    top: parent.top
                    bottom: parent.bottom
                    right: parent.right
                    left: searchIcon.right
                    leftMargin: 20
                }

                verticalAlignment: Text.AlignVCenter
                font.pixelSize: 16

            }
        }

        Image {
            id: lockIcon
            anchors {
                left: parent.left
                top: parent.top
                margins: 10
            }
            width: parent.width / 30
            fillMode: Image.PreserveAspectFit
            source: (systemHandler.carLocked ? "asset/lock.png" : "asset/unlock.png")
            MouseArea {
                anchors.fill: parent
                onClicked: systemHandler.setCarLocked(!systemHandler.carLocked)
            }
        }
    }

    Rectangle {
        id: leftScreen
        anchors {
            top: parent.top
            left: parent.left
            right: rightScreen.left
            bottom: bottomBar.top
        }
        
        Image {
            id: carModel
            source: "asset/carModel.jpg"
            anchors.centerIn: parent
            fillMode: Image.PreserveAspectFit
            width: parent.width
        }
    }
}