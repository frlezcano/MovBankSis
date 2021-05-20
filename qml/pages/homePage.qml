import QtQuick 2.0
import QtQuick.Controls 2.15
import "../controls"
import QtQuick.Layouts 1.0

Item {
    Rectangle {
        id: rectangle
        color: "#2c313c"
        anchors.fill: parent
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 0

        Rectangle {
            id: rectangleVisible
            color: "#1d2128"
            radius: 10
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 112
            anchors.rightMargin: 50
            anchors.leftMargin: 50
            anchors.topMargin: 28

            Label {
                id: labelTextName
                y: 8
                height: 25
                color: "#5c667d"
                text: qsTr("Municipalidad de Asuncion")
                anchors.left: parent.left
                anchors.right: parent.right
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.leftMargin: 10
                anchors.rightMargin: 10
                font.pointSize: 14
            }

            Label {
                id: labelDate
                y: 57
                height: 25
                color: "#55aaff"
                text: qsTr("Date")
                anchors.left: parent.left
                anchors.right: parent.right
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.rightMargin: 10
                anchors.leftMargin: 10
                font.pointSize: 12
            }

            ScrollView {
                id: scrollView
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: labelDate.bottom
                anchors.bottom: parent.bottom
                clip: true
                anchors.rightMargin: 10
                anchors.leftMargin: 10
                anchors.bottomMargin: 16
                anchors.topMargin: 27

                Text {
                                        id: textHome
                                        height: 208
                                        color: "#a9b2c8"
                                        text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html>\n\t<head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n\t\tp, li { white-space: pre-wrap; }\n\t</style></head>\n\t<body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n\t\t<p></p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\"><span style=\"font-weight: 600;\">Bienvenido al Sistema de Registro de Movimientos Bancarios</span></p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\">Version 1.01, Mayo 2021</p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\">&nbsp;</p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\">Copyright (c) 2021 <span style=\"font-weight: 600;\">TIC's - Unidad de Desarrollo</span></p>\n\t\t<p style=\"-qt-paragraph-type: empty; -qt-block-indent: 0; text-indent: 0px; font-weight: 600; margin: 0px;\">&nbsp;</p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\">Instrucciones generales para importar una planilla:</p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\">&nbsp;</p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\"><strong>1-</strong> Seleccionar el archivo Excel (<span style=\"color: #ff0000;\">previamente formateado!</span>) en su disco duro.</p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\"><strong>2-</strong> Validar en la vista previa los datos pre-procesados.</p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\"><strong>3-</strong> Importar los registros a la Base de Datos del SITV2</p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\">&nbsp;</p>\n\t\t<p style=\"-qt-block-indent: 0; text-indent: 0px; margin: 0px;\">Al finalizar el proceso de importaci&oacute;n de registros el sistema le proporcionar&aacute; un resume de la cantidad de registros procesados y m&aacute;s informaci&oacute;n que podr&aacute; utilizar para identificar este proceso en particular.</p>\n</body></html>"
                                        anchors.fill: parent
                                        font.pixelSize: 12
                                        anchors.leftMargin: 0
                                        anchors.topMargin: -49
                                        anchors.bottomMargin: 19
                                        anchors.rightMargin: 391
                                        textFormat: Text.RichText
                }
            }

            Label {
                id: labelTextName1
                y: 33
                height: 25
                color: "#5c667d"
                text: qsTr("Direccion General de Administracion y Finanzas")
                anchors.left: parent.left
                anchors.right: parent.right
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.pointSize: 14
                anchors.rightMargin: 10
                anchors.leftMargin: 10
            }
        }

        Rectangle {
            id: rectangleTop
            color: "#495163"
            radius: 10
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 23
            GridLayout {
                anchors.fill: parent
                CustomTextField {
                    id: textField
                    Layout.fillWidth: true
                    Keys.onEnterPressed: {
                                backend.welcomeText(textField.text)
                            }
                    Keys.onReturnPressed: {
                                backend.welcomeText(textField.text)
                            }
                    placeholderText: "Archivo excel"
                }

                CustomButton {
                    id: btnChangeName
                    visible: false
                    text: "Excel a procesar"
                    Layout.fillWidth: true
                    Layout.maximumWidth: 200
                    Layout.preferredHeight: 40
                    onClicked: {
                                backend.welcomeText(textField.text)
                            }
                    Layout.preferredWidth: 250
                }

                Switch {
                    id: switchHome
                    text: qsTr("Switch")
                    onToggled: {
                                backend.showHideRectangle(switchHome.checked)
                            }
                    checked: true
                    Layout.preferredHeight: 40
                    Layout.preferredWidth: 68
                }
                columns: 3
                rows: 1
                anchors.rightMargin: 10
                anchors.leftMargin: 10
            }
            anchors.rightMargin: 50
            anchors.topMargin: 388
            anchors.leftMargin: 50
        }
    }

    Connections{
        target: backend

        function onSetName(name){
            labelTextName.text = name
        }

        function onPrintTime(time){
            labelDate.text = time
        }

        function onIsVisible(isVisible){
            rectangleVisible.visible = isVisible
        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:800}D{i:7}D{i:8}
}
##^##*/
