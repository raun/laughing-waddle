function lazyLoad(t,o){var n=window.document;b=n.body,e=n.createElement("script"),e.src=t,b.appendChild(e),o&&$(e).on("load",o)}var clevertap={event:[],profile:[],account:[]};clevertap.account.push({id:"RZ5-WW6-754Z"}),function(){var t=document.createElement("script");t.type="text/javascript",t.async=!0,t.src=("https:"==document.location.protocol?"https://d2r1yp2w7bby2u.cloudfront.net":"http://static.clevertap.com")+"/js/a.js?v=0";var e=document.getElementsByTagName("script")[0];e.parentNode.insertBefore(t,e)}(),window.fbAsyncInit=function(){FB.init({appId:"116624972004064",xfbml:!0,version:"v2.3"})},function(t,e,o){var n,a=t.getElementsByTagName(e)[0];t.getElementById(o)||(n=t.createElement(e),n.id=o,n.src="//connect.facebook.net/en_US/sdk.js",a.parentNode.insertBefore(n,a))}(document,"script","facebook-jssdk"),console&&console.log&&console.log("%c%s%c%s%c%s%c%s","font-size:16px;font-family:helvetica;color: #da1f3c","Hmmm! You are a developer and seemingly a frontend developer. Here is a coding problem for you:","font-family: monospace;color:darkgreen;font-size: 13px;font-style: normal;font-variant: normal;font-weight: 400;line-height: 18.5714302062988px;","\n\n(function(you){\n	if(you.loveToWorkOnUI && you.wantToTakeItFurther) {\n		you.sendYourResume('","color:blue","rohit@furlenco.com","color:darkgreen","');\n		return you.awesomeFeeling();\n	} else {\n		return you.boringJob();\n	}\n})();"),window.__insp=window.__insp||[],__insp.push(["wid",167314216]),function(){function t(){if("undefined"==typeof window.__inspld){window.__inspld=1;var t=document.createElement("script");t.type="text/javascript",t.async=!0,t.id="inspsync",t.src=("https:"==document.location.protocol?"https":"http")+"://cdn.inspectlet.com/inspectlet.js";var e=document.getElementsByTagName("script")[0];e.parentNode.insertBefore(t,e)}}setTimeout(t,500),"complete"!=document.readyState?window.attachEvent?window.attachEvent("onload",t):window.addEventListener("load",t,!1):t()}(),function(){$("[inview-animation]").each(function(){var t=this,e=$(this),o=e.attr("inview-animation");new Waypoint.Inview({element:t,enter:function(t){e.addClass("animated "+o)},offset:"80%"})})}(),$(document).ready(function(){var t=/(iPad|iPhone|iPod)/g.test(navigator.userAgent);t&&$("body").addClass("iOS-device")}),$(document).ready(function(){lazyLoad("//d2i9n9psct0730.cloudfront.net/web/production/assets/consumer/ng-code-b5f3fefd41eec25f1cff0500cb3a9207.js",ngInit)}),$(document).ready(function(){var t=$("#my-menu"),e=t.mmenu({extensions:["border-full","pageshadow","theme-white"]},{offCanvas:{}}).data("mmenu");$("#rohit").click(function(){e.open()}),t.find(".navbar-toggle").click(function(){e.close()})}),$(function(){$(window).width()<992&&$.smartbanner({title:"Furlenco",author:"Live Better Now",force:"android",daysHidden:0,price:"FREE",appendToSelector:"body",button:"Download"})});var ResponsiveIO={retina:!1};!function(){var t=function(t){var e=!!t.data("lazy-bg-src"),o=t.data("lazy-src")||t.data("lazy-bg-src"),n=e?"data-bg-src":"data-src";t.attr(n,o)},e=function(e){var o=$(e);t(o),ResponsiveIO.refresh(e),o.data("lazy-loaded",!0)},o={sizeMapping:{mobile:{from:0,to:540,fallback:["tablet","desktop"]},tablet:{from:541,to:980,fallback:["desktop","mobile"]},desktop:{from:981,to:1e4,fallback:["tablet","mobile"]}},figureOutDeviceSize:function(){var t=$(document).width(),e="";return _.forEach(this.sizeMapping,function(o,n){t>o.from&&t<o.to&&(e=n)}),e},"do":function(t){var e=this,o=this.figureOutDeviceSize();$("[data-responsiwize]").each(function(){var n=$(this),a=n.data("responsiwize-src-"+o);if(!a)for(var i=0,c=e.sizeMapping[o].fallback;!a;){var r=c[i++];a=n.data("responsiwize-src-"+r)}a&&(1==n.data("lazy-loaded")?n.is("img")?n.attr("data-src",a):n.attr("data-bg-src",a):n.is("img")?n.attr("data-lazy-src",a):n.attr("data-lazy-bg-src",a),t&&t.reload&&n.trigger("lazyLoadRequest"))})}};$(document).ready(function(){o["do"]({reload:!1}),$(document).on("lazyLoadRequest","img[data-lazy-src], [data-lazy-bg-src]",function(t,o){e(this)}),$(window).on("resize",_.debounce(function(){o["do"]({reload:!0})},100))}),$(window).load(function(){$("img[data-lazy-src]").each(function(){e(this)})})}(),$(document).ready(function(){"use strict";var t=$(".navbar.custom-nav"),e=$(".offer-nav"),o=$("#smartbanner.shown"),n=$(document);if(t.affix({offset:{top:(e.length?29:0)+(o.length?70:0)}}),document.body.scrollWidth>767&&e.affix({offset:{top:29}}),$("#my-menu").removeClass("hide"),$(".scrollToTop").click(function(){return $("body").animate({scrollTop:0},600),!1}),$(".lenco-stack-items").length>0){var n=$(document),a=793;window.onscroll=_.throttle(function(){n.scrollTop()<=a?($(".scrollToTop").css("opacity","0"),$(".addToCart-sticky").css("opacity","0"),$(".stickyTopPdpBar").css({opacity:0,display:"none"})):($(".scrollToTop").css("opacity","1"),$(".addToCart-sticky").css("opacity","1"),$(".stickyTopPdpBar").css({opacity:1,display:"block"}))},100)}$(document).on("click",".pdp-preview-link",function(t){t.preventDefault();var e=$(this).attr("data-room"),o=$(this).attr("data-item"),n=$('a[href="#room_'+e+'"]');n.length&&n[0].click();var a,i,c=$(".roomItem"+o+":visible");c.length?a=c.offset().top:(a=$("#lenco_other_items_carousel_"+e).offset().top,i=$(".other_item"+o).attr("data-slick-index")),setTimeout(function(){$("body").animate({scrollTop:a-250},600),void 0!=i&&$("#lenco_other_items_carousel_"+e).slick("slickGoTo",i)},100)})}),window.twttr=function(t,e,o){var n,a=t.getElementsByTagName(e)[0],i=window.twttr||{};return t.getElementById(o)?i:(n=t.createElement(e),n.id=o,n.src="https://platform.twitter.com/widgets.js",a.parentNode.insertBefore(n,a),i._e=[],i.ready=function(t){i._e.push(t)},i)}(document,"script","twitter-wjs");