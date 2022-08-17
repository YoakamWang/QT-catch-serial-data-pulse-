#ifndef PICTUREDAO_H
#define PICTUREDAO_H

#include <memory>
#include <vector>
#include <QString>

class QSqlDatabase;

class PictureDao
{
public:
    explicit PictureDao(QSqlDatabase& database);
//    void init() const;

//    void addPictureInAlbum(int albumId, Picture& picture) const;
//    void removePicture(int id) const;
//    void removePicturesForAlbum(int albumId) const;
    QString picturePath() const;

private:
    QSqlDatabase& mDatabase;
};

#endif // PICTUREDAO_H
