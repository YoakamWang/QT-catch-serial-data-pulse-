#ifndef SHOWDIALOG_H
#define SHOWDIALOG_H
#include <QImageReader>
#include <QDialog>

namespace Ui {
class showDialog;
}

class showDialog : public QDialog
{
    Q_OBJECT

public:
    explicit showDialog(QWidget *parent = nullptr);
    ~showDialog();

private slots:
    void on_showButton_clicked();

private:
    Ui::showDialog *ui;
};

#endif // SHOWDIALOG_H
