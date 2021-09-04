$(function(){
  $('.moon').each(function(index){
    var phase = $(this).attr('phase');
    var moon_size = calculateMoonSize($(this), phase);
    var moon_colors = calculateMoonColors(phase);

    updateMoon($(this), moon_size, moon_colors);
  });
});


// Math.radians = function(degrees) {
//   return degrees * Math.PI / 180;
// };

const max_phase = 27;
const fullmoon_phase = 14;

function calculateMoonSize(moon_object, phase){
  var current_moon_size = moon_object.width();
  var calculated_moonlight_size = 0;

  var moonlight_percentage =  100 * phase / fullmoon_phase;

  if (moonlight_percentage <= 100){
    calculated_moonlight_size = current_moon_size * moonlight_percentage / 100;
  }
  else{
    calculated_moonlight_size = current_moon_size * (moonlight_percentage - 100) / 100;
  }

  return calculated_moonlight_size;
}

function calculateMoonColors(phase){
  const moon_color = '#45484B';
  const moonlight_color = '#fcef8d';

  var colors = {
    'moon': moon_color,
    'moonlight': moonlight_color
  };

  if (phase <= fullmoon_phase){
    colors.moon = moon_color;
    colors.moonlight = moonlight_color;
  }
  else{
    colors.moon = moonlight_color;
    colors.moonlight = moon_color;
  }

  return colors;
}

function updateMoonColors(moon_object, colors){
  // moon-left
  moon_object.find('.moon-left .bg').css({
    'stroke':colors.moon,
    'fill':colors.moon
  });
  moon_object.find('.moon-left .fg').css({
    'stroke':colors.moonlight,
    'fill':colors.moonlight
  });
  // moon-right
  moon_object.find('.moon-right .bg').css({
    'stroke':colors.moonlight,
    'fill':colors.moonlight
  });
  moon_object.find('.moon-right .fg').css({
    'stroke':colors.moon,
    'fill':colors.moon
  });

}

function updateMoon(moon_object, phase, colors){
  var current_moon_size = moon_object.width();
  updateMoonColors(moon_object, colors);

  var phaseScale = 1,
      phaseTrans = (current_moon_size/2),
      phaseRight = 0;

  if(phase <= (current_moon_size/2)) {
    phaseRight = (1-phase/(current_moon_size/2));
  }
  moon_object.find('.moon-right .fg').css({
    'transform':'scaleX(' + phaseRight + ')'
  });

  if(phase >= (current_moon_size/2)) {
    phaseScale = (1-(phase-(current_moon_size/2))/(current_moon_size/2));
    phaseTrans = (current_moon_size/2)*phaseScale;
  }
  moon_object.find('.moon-left .fg').css({
    'transform':'translate('+phaseTrans+'px,0) scaleX(' + (1-phaseScale) + ')'
  });
}
