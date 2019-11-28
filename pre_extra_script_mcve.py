Import("env")
import os

# access to global construction environment
#print env

# Dump construction environment (for debug purpose)
#print env.Dump()

# append extra flags to global build environment
# which later will be used to build:
# - project source code
# - frameworks
# - dependent libraries
env.Append(CPPDEFINES=[
  "PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_190703",
  "ESPEASY_MCVE_BUILD"
  # ,"NO_HTTP_UPDATER"
  # ,("WEBSERVER_RULES_DEBUG", "0")
])
if os.path.isfile('src/Custom.h'):
  env['CPPDEFINES'].append("USE_CUSTOM_H")
else:
  env['CPPDEFINES'].extend([
        "USES_P001",  # Switch
        "USE_SETTINGS_ARCHIVE"
  ])

print(env['CPPDEFINES'])
print()
