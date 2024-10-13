document.addEventListener('DOMContentLoaded', init);

function init() {
    //Leaflet Map
    const map = L.map('map').setView([-40.9006,174.886], 6);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright"> OpenStreetMap contributors'
    }).addTo(map);

    // Fetch data from the API - GET Request
    const fetchGetRequest = async (url, func) => {
        try{
            const response = await fetch(url);
            const data = await response.json();
            return func(data);
        } catch (error) {
            console.log(error.message);
        }
    }

    const selectedPointStyle={
        stroke: true,
        radius: 11,
        color:'black',
        weight: 2,
        opacity: 1,
        fillColor: 'white',
        fillOpacity: 1,
    }

    
    let lastClickedFeature;
    const styleGeoJSONOnClick = (places) => {
        places.on('click', (e)=>{
            if (lastClickedFeature){
             //   places.resetStyle(lastClickedFeature);
            }
            lastClickedFeature = e.layer;
            
        //    console.log(e)
       //     e.layer.setStyle(selectedPointStyle);
        }) 
    }

    const cityPiontStyle = {
        radius: 8,
        fillColor: "#ff7800",
        color: "#000",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
    }
    var nearbyCitiesGeoJSONLayer;
    const addNearbyCities = (geojson)=>{
        if (nearbyCitiesGeoJSONLayer){
            map.removeLayer(nearbyCitiesGeoJSONLayer);
        }
        nearbyCitiesGeoJSONLayer = L.geoJSON(geojson, {
            pointToLayer: (feature, latlng) => {
                return L.circleMarker(latlng, cityPiontStyle);
            },
            onEachFeature: (feature, layer) => {
                const cityname = feature.properties.name;
                const proximity = feature.properties.proximity;
                layer.bindPopup(`city name: ${cityname}, <br/> proximity: ${proximity} km`);
            }
        }).addTo(map);

    }

    const addNearbyCitiesLogic = (id) => {
        let url = `/api/v1/cities/?placeid=${id}`;
        fetchGetRequest(url, addNearbyCities);
    }

    const placeImageElement = document.getElementById('placeimage');
    const menuTitleElement = document.getElementById('menu_title');
    const menuTextElement = document.getElementById('menu_text');
    const onEachFeatureHandler = (feature, layer) => {
        let placeName = feature.properties.place_name;
        layer.bindPopup(`<br/><center><b>${placeName}</b></center>`);
        
        layer.on('click', (e) => {
            let featureImage = feature.properties.image;
            let featureDescription = feature.properties.description;
            menuTitleElement.innerHTML = `${placeName}`;
            placeImageElement.setAttribute('src', featureImage);
            menuTextElement.innerHTML = featureDescription;

            let feaureID = feature.properties.pk;
            addNearbyCitiesLogic(feaureID)

        });
   
    }

    const addAllPlacesToMap = (data) => {
        let places = L.geoJSON(data, {
            onEachFeature: (feature, layer) => {
                onEachFeatureHandler(feature, layer);
            }
        }
        ).addTo(map);
        
        styleGeoJSONOnClick(places);
       
    }

    fetchGetRequest('/api/v1/places', addAllPlacesToMap);



}