# Test

{
    'variables': {
    },
    'targets': [
        {
            'target_name': 'electron-celt-<@(target_arch)',
            'dependencies': [
                'deps/binding.gyp:libcelt'
            ],
            'cflags': [
                '-pthread',
                '-fno-exceptions',
                '-fno-strict-aliasing',
                '-Wall',
                '-Wno-unused-parameter',
                '-Wno-missing-field-initializers',
                '-Wextra',
                '-pipe',
                '-fno-ident',
                '-fdata-sections',
                '-ffunction-sections',
                '-fPIC'
            ],
            'defines': [
                'LARGEFILE_SOURCE',
                '_FILE_OFFSET_BITS=64',
                'WEBRTC_TARGET_PC',
                'WEBRTC_LINUX',
                'WEBRTC_THREAD_RR',
                'EXPAT_RELATIVE_PATH',
                'GTEST_RELATIVE_PATH',
                'JSONCPP_RELATIVE_PATH',
                'WEBRTC_RELATIVE_PATH',
                'POSIX',
                '__STDC_FORMAT_MACROS',
                'DYNAMIC_ANNOTATIONS_ENABLED=0'
            ],
            'include_dirs': [
                "<!(node -e \"require('nan')\")",
                "<!(node -e \"require('electron-updater-tools')\")"
            ],
            'sources': [
                'src/node-celt.cc',
            ],
            'link_settings': {
                'ldflags': [
                ],
                'libraries': [
                ]
            },
            'target_conditions': [
                [ 'OS=="win"', {
                    'libraries': [
                        '-lShlwapi.lib'
                    ],
                    'msvs_settings': {
                        'VCLinkerTool': {
                            'DelayLoadDLLs': [ 'node.dll', 'iojs.exe', 'node.exe' ],
                            # Don't print a linker warning when no imports from either .exe
                            # are used.
                            'AdditionalOptions': [ '/ignore:4199' ],
                        },
                    },
                }],
            ]
        }
    ]
}
