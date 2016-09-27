
translate([5,55/2,30])
difference(){
    cube([10, 55, 16], center=true);
    cube([8.5, 52.5, 18], center=true);
}


translate([11,27/2,-1*17/2])
difference(){
    cube([22, 27, 17], center=true);
    cube([17, 19.2, 12+7], center=true);
    translate([0, 10, 0])
        cube([8, 20, 12+7], center=true);
}
translate([11,20+27/2,-1*17/2-4.5])
difference(){
    cube([12, 20, 8], center=true);
    cube([8, 21, 12], center=true);
}




hull(){
    cube([(22-17)/2, 27, 0.1]);
    translate([0,0,30-15/2])
        cube([(10-8.2)/2, 55, 0.1]);

}


hull(){
    translate([22-(22-17)/2,0,0])
        cube([(22-17)/2, 27, 0.1]);
    translate([10-(10-8.2)/2,0,30-15/2])
        cube([(10-8.2)/2, 55, 0.1]);

}

hull(){
    cube([22, (27-19.2)/2, 0.1]);
    translate([0,0,30-15/2])
        cube([10, (55-52.5)/2, 0.1]);

}

hull(){
    translate([0,27-(27-19.2)/2,0])
    cube([22, (27-19.2)/2, 0.1]);
    translate([0,55-(55-52.5)/2,30-15/2])
        cube([10, (55-52.5)/2, 0.1]);

}