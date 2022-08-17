#include "showdialog.h"
#include "ui_showdialog.h"
#include <QDir>
#include "mainwindow.h"

QString MainWindow::filepath;

showDialog::showDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::showDialog)
{
    ui->setupUi(this);
//    QImageReader reader("/home/yj/Pictures/result/result1.png");
//    reader.setDecideFormatFromContent(true);
//    QPixmap pic=QPixmap::fromImage(reader.read());
    QPixmap pic("./result1.png");
    ui->label->setPixmap(pic);

}

showDialog::~showDialog()
{
    delete ui;
}

void showDialog::on_showButton_clicked()
{
    QPixmap pic;
  // QString strPath=QDir::currentPath()+"/result.png";
    QString strPath=MainWindow::filepath;
    // qDebug()<<strPath;
    if(pic.load(strPath))
    {
        ui->label->setPixmap(pic);
    }
}
