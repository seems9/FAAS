var fs = require("fs");
var str = process.argv.slice(2);

//console.log(str.toString().replace(/[\[\]']/g,'' ));

var new_arg = str.toString().replace(/[\[\]']/g,'' )
var contents = fs.readFileSync("products.json");
var jsonContent = JSON.parse(contents);
for (var i = 0; i < jsonContent.length; i++){

       var o = jsonContent[i];
       if(o['sku'] == new_arg) {
       	console.log(o)
       }

       
}

