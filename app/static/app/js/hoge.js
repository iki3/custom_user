
    function initMap() {

      // マップの初期化
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 16,
        center: {lat: 33.232647, lng: 131.651055}
      });

      // クリックイベントを追加
      map.addListener('click', function(e) {
        getClickLatLng(e.latLng, map);
      });
    }

    function getClickLatLng(lat_lng, map) {

      // 座標を表示
      document.getElementById('lat').textContent = lat_lng.lat();
      document.getElementById('lng').textContent = lat_lng.lng();
//    var icon = new google.maps.MarkerImage('president_furukawa.jpg',
//    new google.maps.Size(200,200),
//    new google.maps.Point(0,0),
//    new google.maps.Point(19,51)
//  );
      // マーカーを設置
      var marker = new google.maps.Marker({
        position: lat_lng,
        map: map,
        icon: icon

      });

      // 座標の中心をずらす
      // http://syncer.jp/google-maps-javascript-api-matome/map/method/panTo/
      map.panTo(lat_lng);
    }
