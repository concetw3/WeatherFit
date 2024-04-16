const axios = require('axios');
const fs = require('fs');

const getWeatherForecast = async (latitude, longitude) => {
    const headers = { 'User-Agent': 'Mozilla/5.0' };
    const response = await axios.get(`https://api.met.no/weatherapi/locationforecast/2.0/complete?lat=${latitude}&lon=${longitude}`, { headers });
    return response.data.properties.timeseries;
};

const getWeatherDetails = (timeseries) => {
    const nextHour = timeseries[0].data.next_1_hours;
    const precipitation = nextHour.details.precipitation_amount || 0;
    const symbolCode = nextHour.summary.symbol_code;
    const temperature = timeseries[0].data.instant.details.air_temperature;
    return { temperature, precipitation, symbolCode };
};

const loadJsonData = (filePath) => {
    const rawData = fs.readFileSync(filePath);
    return JSON.parse(rawData);
};

const findKeys = (node, kv) => {
    let found = [];
    if (Array.isArray(node)) {
        node.forEach(item => found = found.concat(findKeys(item, kv)));
    } else if (node !== null && typeof node === 'object') {
        if (kv in node) found.push(node[kv]);
        Object.values(node).forEach(value => {
            found = found.concat(findKeys(value, kv));
        });
    }
    return found;
};

const selectClothing = (temperature, precipitation, symbolCode, data) => {
    let outfit = {};

    outfit.Headwear = temperature <= 0 ? randomChoice(data.hovedbeklaedning.huer) : randomChoice(data.hovedbeklaedning.kasketter);

    const jakkerData = data.jakker;
    if (precipitation >= 1) {
        const jakkerVandtaette = findKeys(jakkerData, 'vandtaette');
        outfit.Jacket = randomChoice(jakkerVandtaette);
    } else if (temperature <= 3) {
        const jakkerVarme = findKeys(jakkerData, 'varme');
        outfit.Jacket = randomChoice(jakkerVarme);
    } else if (temperature <= 10) {
        const jakkerOvergang = findKeys(jakkerData, 'overgang');
        outfit.Jacket = randomChoice(jakkerOvergang);
    } else {
        const jakkerLette = findKeys(jakkerData, 'lette');
        outfit.Jacket = randomChoice(jakkerLette);
    }

    outfit.Footwear = precipitation > 0 ? randomChoice(data.sko.vandtaette) : randomChoice(temperature <= 0 ? data.sko.varme : data.sko.lette);

    return outfit;
};

const randomChoice = (array) => {
    return array[Math.floor(Math.random() * array.length)];
};

const main = async () => {
    const latitude = 55.67, longitude = 12.56;
    const timeseries = await getWeatherForecast(latitude, longitude);
    const { temperature, precipitation, symbolCode } = getWeatherDetails(timeseries);

    const clothingData = {
        hovedbeklaedning: loadJsonData('./Json/hovedbeklaedning.json'),
        jakker: loadJsonData('./Json/jakker.json'),
        bukser: loadJsonData('./Json/bukser.json'),
        sko: loadJsonData('./Json/sko.json'),
        // Add other categories as needed
    };

    const outfit = selectClothing(temperature, precipitation, symbolCode, clothingData);

    console.log("Recommended Outfit based on current weather conditions:");
    Object.keys(outfit).forEach(key => {
        console.log(`${key}: ${outfit[key].navn}`);
    });
};

main();