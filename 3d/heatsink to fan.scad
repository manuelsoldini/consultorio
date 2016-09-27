
translate([20,0,0])
difference(){
    cube([10, 55, 16], center=true);
    cube([8.5, 52.5, 18], center=true);
}


translate([-20,0,0])
difference(){
    cube([22, 27, 10], center=true);
    cube([17, 19.2, 12], center=true);
    translate([0, 10, 0])
        cube([8, 20, 12], center=true);
}
translate([-20,20,-1])
difference(){
    cube([12, 20, 8], center=true);
    cube([8, 21, 12], center=true);
}