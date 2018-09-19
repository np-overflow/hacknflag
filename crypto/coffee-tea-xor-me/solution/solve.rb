#!/usr/bin/env ruby
ciphertext = File.read("ciphertext.txt")
flag = "H"
(ciphertext.length-1).times do |i|
    decrypted_char = (ciphertext[i].ord ^ flag[i].ord).chr
    flag += decrypted_char
end
puts flag