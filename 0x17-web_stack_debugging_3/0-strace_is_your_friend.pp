# Set the path to the file to be modified
$file_path = '/var/www/html/wp-settings.php'

# Execute a command to replace a line in the file using sed
# The 's/phpp/php/g' argument tells sed to replace all occurrences of 'phpp' with 'php'
# The ${file_path} argument is the path to the file to be modified
# The '-i' flag tells sed to edit the file in place
command => "sed -i 's/phpp/php/g' ${file_path}",

# Set the search path for the command to be executed
# In this case, the command may be located in /bin or /usr/bin
path    => ['/bin','/usr/bin']
