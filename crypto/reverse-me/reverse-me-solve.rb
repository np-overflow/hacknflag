#!/usr/bin/env ruby
cipher = File.read("ciphertext.txt")
flag = ""
cipher.length.times do |i|
    decrypted_char = (cipher[i].ord + 10) ^ 6
    flag += decrypted_char.chr
end
puts flag