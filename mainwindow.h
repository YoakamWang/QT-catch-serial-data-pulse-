#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QLabel>
#include <QMainWindow>
#include "Chart.h"
#include "settingsdialog.h"
#include "showdialog.h"
#include "PictureDao.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE


class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    static int inner; //Transfer the serial data from mainwindow to chart.
    static int moto;
    static int outer;
//    static QString filepath;
//    struct SerialData{
//        int enround;
//        int motoround;
//        int biground;
//    };
//    SerialData serialdata() const;
   MainWindow(QWidget *parent = nullptr);
   void clearInner();
   void clearMoto();
   void clearOuter();


    ~MainWindow();

private slots:
    void openSerialPort();
    void closeSerialPort();
    void readData();
    void writeData();
    void OnReadData();
    void on_clearInnerButton_clicked();

//    void on_clearouterButton_clicked();

//    void on_clearmotoButton_clicked();

    void on_startButton_clicked();

    void process_python(QString,QString);


    void on_pushButton_2_clicked();

    void on_lineEdit_editingFinished();

signals:
//    void sendDataChart(int encoderround,int motoround,int biground);
    void filePath(const QString,const QString);
    void picpath(const QString);
private:
    void showStatusMessage(const QString &message);
private:
    Ui::MainWindow *ui;
    SettingsDialog *m_settings = nullptr;
    showDialog *m_show=nullptr;
    QSerialPort *m_serial = nullptr;
    QLabel *m_status = nullptr;
    QFile m_file_save;
    QTimer wriDataTimer;
    QTimer crashTimer;
    bool flag;
    QProcess* process1;
    //PictureDao *mpicture_dao= nullptr;
    //SerialData m_serialData;

};
#endif // MAINWINDOW_H
