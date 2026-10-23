// Renders Open Peeps characters (CC0, Pablo Stanley) to static SVG.
// Setup: npm i react@18.3.1 react-dom@18.3.1 && npm pack @opeepsfun/open-peeps,
// then copy the package's build/ folder next to this script as ./op and create ./out.
// Run: node peeps-cast.js, then optimise with: npx svgo@3.3.2 -f out -p 1
const React=require("react"),{renderToStaticMarkup:r}=require("react-dom/server");const fs=require("fs");
const O=__dirname+"/op"; const req=p=>require(O+"/"+p).default;
const el=(p,o)=>r(React.createElement(req(p),o||{}));
// neck positions (body coords) measured from renders
const NECK={ "body/standing/WalkingColorTee":[740,0], "body/standing/Dancer":[742,0], "body/standing/PointingFingerColorPants":[740,0], "body/standing/EasingColorTee":[740,0], "body/standing/RestingColorTee":[740,0], "body/sitting/Bike":[1455,0], "body/standing/ShirtColorTee":[740,0] };
function person(id,{body,bodyOpt,head,headOpt,face,faceOpt,beard,beardOpt,acc}){
  const C=req(body).config; const [nx,ny]=NECK[body];
  const hx=nx-270, hy=ny-449;
  const svg=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="${Math.min(0,hx-40)} ${hy-20} ${Math.max(C.width,hx+700)-Math.min(0,hx-40)} ${C.height-hy+20}" overflow="visible">`+
    `<g>${el(body,bodyOpt)}</g><g transform="translate(${hx},${hy})">${el("head/"+head,headOpt)}<g transform="translate(189,176)">${el("face/"+face,faceOpt)}</g>`+
    (beard?`<g transform="translate(${495-342},${518-190})">${el("beard/"+beard,beardOpt)}</g>`:"")+
    (acc?`<g transform="translate(${419-342},${421-190})">${el("accessory/"+acc,{})}</g>`:"")+`</g></svg>`;
  fs.writeFileSync(`out/${id}.svg`,svg);
}
fs.mkdirSync("out",{recursive:true});
const SK=["#D9A07A","#B9794A","#8D5A3B","#E8B794"];
person("amira",{body:"body/standing/WalkingColorTee",bodyOpt:{skinColor:SK[0],topColor:"#F2B33D",shoesColor:"#fff"},head:"Hijab",headOpt:{hijabColor:"#13934A",skinColor:SK[0]},face:"Smile"});
person("karim",{body:"body/standing/PointingFingerColorPants",bodyOpt:{skinColor:SK[1],pantsColor:"#0F1F5C",shoesColor:"#fff"},head:"ShortTwo",headOpt:{skinColor:SK[1]},face:"Calm",beard:"Chin"});
person("giulia",{body:"body/standing/Dancer",bodyOpt:{skinColor:SK[3],topColor:"#E1262D",pantsColor:"#0F1F5C",shoesColor:"#fff"},head:"LongCurly",headOpt:{skinColor:SK[3]},face:"SmileLOL"});
person("yousef",{body:"body/sitting/Bike",bodyOpt:{skinColor:SK[2],topColor:"#fff",jacketColor:"#0F1F5C",bikeFrameColor:"#13934A",shoesColor:"#fff"},head:"ShortOne",headOpt:{skinColor:SK[2]},face:"Cute"});
person("lina",{body:"body/standing/EasingColorTee",bodyOpt:{skinColor:SK[0],topColor:"#fff",jacketColor:"#5B8DEF",shoesColor:"#fff"},head:"MediumStraight",headOpt:{skinColor:SK[0]},face:"Smile"});
person("omar",{body:"body/standing/RestingColorTee",bodyOpt:{skinColor:SK[1],topColor:"#13934A",shoesColor:"#fff"},head:"ShortThree",headOpt:{skinColor:SK[1]},face:"BigSmile",beard:"Full"});
