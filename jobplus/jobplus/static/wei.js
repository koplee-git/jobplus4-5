$(function(){
var imgSlider = $('.imageSlider'),
    imageBox = imgSlider.children(".imageBox"),
    titleBox = imgSlider.children(".titleBox"),
    titleSrr = titleBox.children(".p"),
    icoBox = imgSlider.chilren(".icoBox"),
    icoArr = icoBox.children("span"),
    imageWidth = imgSlider.width(),
    imageNum = imageBox.children("a").length,
    imageReelWith = imageWidth * imageNum,
    activeID=parseInt(icoBox.children(".ative").attr("rel")),
    nextID=0,
    setIntervalID,
    intervalTime = 4000,
    imageSpeed = 500,
    titleSpeed = 250;

imageBox.css({"width":imageReelWidth + "px"});
alert("ok")
var rotate = function(clickID){
    if (clickID)
    {
        nextID = clickID;
    }
    else{
        nextID = activeID <= imageNum -1 ? activeID + 1 :1;

    }
$(icoArr[activeID-1]).removeClass("active");
$(icoArr[nextID-1]).addClass("active");

$(titleArr[activeID-1]).animate(
    {bottom:"-40px"},
    titleSpedd,
    function(){
        $(titleArr[nextID-1]).animate({bottom:"0px"},titleSpeed);
        }
);
imageBox.animate({ left:"-" + (nextID -1) * imageWidth + "px"} , imageSpeed);
activeID = nextID;
};
setIntervalID = setINterval(rotate,intervalTime)
imageBox.hover(
    function(){
    clearInterval(setIntervalID);
    },
    function(){
        setIntervalID = setInterval(rotate,intervalTime);
        }
            );
icoArr.on("click",function(){
    clearInterval(setIntervalID);
    var clickID = parseInt($(this).attr("rel"));
    rotate(clickID);
    setIntervalID = setInterval(rotate,intervalTime);
    });

});
