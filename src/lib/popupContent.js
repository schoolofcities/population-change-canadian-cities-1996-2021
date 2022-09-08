import ct from "../assets/ct-pts.geo.json";

function popupContent(ctuid) {
    
    var data = ct.features.filter(ct => ct.properties.ctuid === ctuid)[0];
    var pop21 = data.properties.pop21;
    var pop96 = data.properties.pop96;
    console.log(pop21, pop96);
    var html = 

    "<p>2021 Population: <b>" + pop21 + "</b></p>" + 
    "<p>1996 Population: <b>" + pop96 + "</b></p>" +
    "<p>Difference: <b>" + (pop21 - pop96) + "</b></p>" 
    return html
}

export default popupContent;
