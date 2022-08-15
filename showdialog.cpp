#include "showdialog.h"
#include "ui_showdialog.h"

showDialog::showDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::showDialog)
{
    ui->setupUi(this);
    QPixmap pic("/home/yj/Pictures/result/result.png");
    ui->label->setPixmap(pic);
}

showDialog::~showDialog()
{
    delete ui;
}
