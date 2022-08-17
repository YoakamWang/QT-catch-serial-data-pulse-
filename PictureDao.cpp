#include "PictureDao.h"

#include <QSqlDatabase>
#include <QSqlQuery>
#include <QVariant>
#include <QDebug>

#include "DatabaseManager.h"

using namespace std;

PictureDao::PictureDao(QSqlDatabase& database) :
    mDatabase(database)
{
}

//void PictureDao::init() const
//{
//    if (!mDatabase.tables().contains("pictures")) {
//        QSqlQuery query(mDatabase);
//        query.exec(QString("CREATE TABLE pictures")
//        + " (id INTEGER PRIMARY KEY AUTOINCREMENT, "
//        + "album_id INTEGER, "
//        + "url TEXT)");
//        DatabaseManager::debugQuery(query);
//    }
//}

//void PictureDao::addPictureInAlbum(int albumId, Picture& picture) const
//{
//    QSqlQuery query(mDatabase);
//    query.prepare(QString("INSERT INTO pictures")
//        + " (album_id, url)"
//        + " VALUES ("
//        + ":album_id, "
//        + ":url"
//        + ")");
//    query.bindValue(":album_id", albumId);
//    query.bindValue(":url", picture.fileUrl());
//    query.exec();
//    DatabaseManager::debugQuery(query);
//    picture.setId(query.lastInsertId().toInt());
//    picture.setAlbumId(albumId);
//}

//void PictureDao::removePicture(int id) const
//{
//    QSqlQuery query(mDatabase);
//    query.prepare("DELETE FROM pictures WHERE id = (:id)");
//    query.bindValue(":id", id);
//    query.exec();
//    DatabaseManager::debugQuery(query);
//}

//void PictureDao::removePicturesForAlbum(int albumId) const
//{
//    QSqlQuery query(mDatabase);
//    query.prepare("DELETE FROM pictures WHERE album_id = (:album_id)");
//    query.bindValue(":album_id", albumId);
//    query.exec();
//    DatabaseManager::debugQuery(query);
//}

QString PictureDao::picturePath() const
{
    QSqlQuery query(mDatabase);
    int mid=1;
    //query.prepare("SELECT * FROM pictures WHERE id = (:id);");
    //query.bindValue(":id", mid);
//    query.prepare("SELECT * FROM pictures WHERE album_id = (:album_id)");
//    query.bindValue(":album_id", albumId);
    query.exec(QString(R"(SELECT url FROM pictures WHERE id='%1';)").arg(mid));
    QString path="";
    DatabaseManager::debugQuery(query);
   // unique_ptr<vector<unique_ptr<Picture>>> list(new vector<unique_ptr<Picture>>());

    if(query.next()) {
        //picture->setAlbumId(query.value("album_id").toInt());
        path=query.value(0).toString();
        //qDebug()<<path;
    }
    return path;
}
