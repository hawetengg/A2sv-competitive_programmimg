class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        output = ""
        for i in range(len(command)):
            if command[i] == "G":
                output += "G"
            elif command[i] == "(" and command[i+1] == ")":
                output += "o"
            elif command[i] == "a":
                output += "al"
        return output

