// user 클래스 ok.
class User {
    constructor (id, tag, createdDate, nickname) {
        this.id = id;
        this.tag = tag;
        this.createdDate = createdDate;
        this.nickname = nickname;
        this.name = `[${tag}] ${nickname}`;
    }
}
// 유저 클래스를 상속 받는 partner 클래스
class Partner extends User {
    customGame() {
        console.log('custom game');
    }
}
// let cho = new Partner(1, '크래프톤', '2020-01-01', '조배');
// cho.customGame(); ok


