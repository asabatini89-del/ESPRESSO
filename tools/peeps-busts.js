// Renders Open Peeps characters (CC0, Pablo Stanley) to static SVG.
// Setup: npm i react@18.3.1 react-dom@18.3.1 && npm pack @opeepsfun/open-peeps,
// then copy the package's build/ folder next to this script as ./op and create ./out.
// Run: node peeps-busts.js, then optimise with: npx svgo@3.3.2 -f out -p 1
const React=require("react"),{renderToStaticMarkup:r}=require("react-dom/server");const fs=require("fs");
const O=__dirname+"/op"; const req=p=>require(O+"/"+p).default; const el=(p,o)=>r(React.createElement(req(p),o||{}));
function bust(id,{body,bodyOpt,head,headOpt,face,beard,acc,dy=0}){
  const svg=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="184 150 940 1190" overflow="visible"><g transform="translate(147,639)">${el("body/effigy/"+body,bodyOpt)}</g><g transform="translate(0,${dy})"><g transform="translate(342,190)">${el("head/"+head,headOpt)}</g><g transform="translate(531,366)">${el("face/"+face)}</g>`+
   (beard?`<g transform="translate(495,518)">${el("beard/"+beard)}</g>`:"")+(acc?`<g transform="translate(419,421)">${el("accessory/"+acc)}</g>`:"")+`</g></svg>`;
  fs.writeFileSync(`out/b-${id}.svg`,svg);
}
const SK=["#D9A07A","#B9794A","#8D5A3B","#E8B794","#C68E68"];
const P={
 amira:{body:"Tee",bodyOpt:{skinColor:SK[0],topColor:"#F2B33D"},head:"Hijab",headOpt:{hijabColor:"#13934A",skinColor:SK[0]}},
 karim:{body:"Hoodie",bodyOpt:{skinColor:SK[1],topColor:"#0F1F5C"},head:"ShortTwo",headOpt:{skinColor:SK[1]},beard:"Chin"},
 lina:{body:"StripedTee",bodyOpt:{skinColor:SK[0],topColor:"#E1262D"},head:"MediumStraight",headOpt:{skinColor:SK[0]}},
 omar:{body:"Jacket",bodyOpt:{skinColor:SK[2],topColor:"#13934A"},head:"ShortThree",headOpt:{skinColor:SK[2]},beard:"Full"},
 mama:{body:"Turtleneck",bodyOpt:{skinColor:SK[4],topColor:"#7A5CA8"},head:"Hijab",headOpt:{hijabColor:"#7A5CA8",skinColor:SK[4]},acc:"Glasses"},
 baba:{body:"ButtonShirt",bodyOpt:{skinColor:SK[1],topColor:"#5B8DEF"},head:"GrayShort",headOpt:{skinColor:SK[1]},beard:"MustacheThin"},
 yasmin:{body:"Coffee",bodyOpt:{skinColor:SK[3],topColor:"#0F1F5C",cupColor:"#fff"},head:"Hijab",headOpt:{hijabColor:"#E1262D",skinColor:SK[3]}}
};
for (const [k,v] of Object.entries(P)){ bust(k+"-worry",{...v,face:"Concerned"}); bust(k+"-happy",{...v,face:"Smile"}); }
bust("yasmin-coffee",{...P.yasmin,face:"EatingHappy"});
