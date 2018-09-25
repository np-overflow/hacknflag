#!/usr/bin/env ruby

#variable declaration
lookup = {A:"ttttt", B:'ttttr', C:'tttbr', D:'tttrr', E:'ttrtt',
    F:'ttrtr', G:'ttrrt', H:'ttrrr', I:'trttt', J:'trttr',
    K:'trtrt', L:'trtrr', M:'trrtt', N:'trrtr', O:'trrrt',
    P:'trrrr', Q:'rtttt', R:'rtttr', S:'rttrt', T:'rttrr',
    U:'rtrtt', V:'rtrtr', W:'rtrrt', X:'rtrrr', Y:'rrttt',
     Z:'rrttr', _:"rrtrt","{" => "rrtrr","}" => "rrrtt"}

cipher = "ttrrrtrrtrttrtrrrtrrtrtttrrtrttrtrrtrrrtrtrtrttrttrrtrttrrttttrttrrtrtrttrttrrrttrrttttrttrrtrtttttrttttttttbrtrrrttrrtrtrrtrtrrtrtrrtrtrrtrtrrtrtrrtrrrrtt"
flag = []

#convert the cipher string into the blocks of 5 chars and joins them together to form an array
a = cipher.chars.each_slice(5).map(&:join)

#decoding begins
a.map{ |block| flag << lookup.key(block)}

puts flag.join