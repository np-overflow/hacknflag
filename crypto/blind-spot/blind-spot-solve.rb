#!/usr/bin/env ruby
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars += chars.downcase
chars += "1234567890"
chars += "!@#$%^&*()_+<>?:,./;{}"
flag = ""
f = File.read("some_text.txt")
f.each_char do | c |
    if chars.include? c
        flag += c
    end
end
puts flag