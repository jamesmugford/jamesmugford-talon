from talon import app
from talon.track.geom import Point2d
from talon_plugins import speech, eye_mouse, eye_zoom_mouse

eye_zoom_mouse.config.screen_area = Point2d(200, 150 )
eye_zoom_mouse.config.img_scale = 4.5

eye_zoom_mouse.toggle_zoom_mouse(1);