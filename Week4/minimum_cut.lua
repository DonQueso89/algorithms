V = {}
E = {}

for line in io.lines("mincut_input.txt")
do
    for n in line:gmatch("(%d+)") do
        print(tonumber(n))
    end
end
