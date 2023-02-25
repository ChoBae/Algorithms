// 헤더 (메뉴탭, 검색창, 프로필) done;
// 왼쪽 aside (홈, 쇼츠,등(개인공간), 보관함(시청기록, 좋아요,등), 구독명단, 등등) done;
// 메인 섹션 영상 (최근에는 분류별로 위에 태그 메뉴가 생겨서 볼수 있게 만든듯) done
<body>
  <div>
    {/* header section*/}
    <header>
      {/* logo section -> 메인로고 클릭시 홈이동 */}
      <logo></logo>
      {/* search section  -> 검색창, 검색버튼*/}
      <div>
        <search></search>
      </div>
      {/* profile section -> 프로필 사진 밑 프로필로 이동*/}
      <div>
        <profile></profile>
      </div>
    </header>
    {/* left aside section */}
    <aside>
      {/* 홈, 쇼츠 , 구독 탭 (아이콘 + text)  */}
      <div>
        {/* map으로 구독 채널 정보를 props로 넣어줘야함 */}
        <taps props={"props.data"} />
      </div>
      {/* 보관함 (보관함,시청기록 , 내 동영상, 나중에 볼 동영상) */}
      <div>
        {/* map으로 구독 채널 정보를 props로 넣어줘야함 */}
        <taps props={"props.data"} />
      </div>
      {/* 구독 명단 (채널 사진 + 이름)*/}
      <div>
        {/* map으로 구독 채널 정보를 props로 넣어줘야함 */}
        <channel props={"props.data"} />
      </div>
    </aside>
    {/* main section  */}
    <section>
      {/* 장르별 탭 */}
      <div>
        {/* map으로 구독 채널 정보를 props로 넣어줘야함 */}
        <taps props={"props.data"} />
      </div>
      {/* 영상 리스트 */}
      <div>
        {/* map으로 구독 채널 정보를 props로 넣어줘야함 */}
        <video props={"props.data"} />
      </div>
    </section>
  </div>
</body>;

// 로고 컴포넌트
const logo = (props) => {
  const link = "location.href=" + props.link + "";
  return (
    <div onClick={link}>
      <img src={props.img}></img>
    </div>
  );
};

// 검색창 컴포넌트
const search = (props) => {
  return (
    <div>
      <input></input>
      <button></button>
    </div>
  );
};

// 프로필 컴포넌트
const profile = (props) => {
  const link = "location.href=" + props.link + "";
  return (
    <div onClick={link}>
      <img src={props.img}></img>
    </div>
  );
};

// 채널 컴포넌트
const channel = (props) => {
  const link = "location.href=" + props.link + "";
  return (
    <div onClick={link}>
      <img src={props.img}></img>
      <div>{props.name}</div>
    </div>
  );
};
// 메뉴탭별 컴포넌트
const taps = (props) => {
  const link = "location.href=" + props.link + "";
  return (
    <div onClick={link}>
      {/* 탭별 이미지 */}
      <img src={props.img}></img>
      <div>{props.title}</div>
    </div>
  );
};
// 영상 컴포넌트
const video = (props) => {
  const link = "location.href=" + props.link + "";
  return (
    <div onClick={link}>
      {/* 영상 이미지 */}
      <img src={props.img}></img>
      <div>{props.title}</div>
      <div>{props.channelName}</div>
      {/* 조회수 */}
      <div>{props.view}</div>
      {/*올린 시간  -> 올린시간부터 지난시간을 구해야해서 나중에 수정 *TODO* */}
      <div>{props.time}</div>
    </div>
  );
};
