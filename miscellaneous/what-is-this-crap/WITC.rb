#!/usr/bin/env ruby
f1 = File.read("text1.txt")
f2 = File.read("text2.txt")
flag1 = ""
flag2 = ""
f1.length.times do |i|
    if f1[i] != f2[i]
        flag1 += f1[i]
        flag2 += f2[i]
    end
end
if flag1[0..3] == "HNF"
    puts flag1
else
    puts flag2
end