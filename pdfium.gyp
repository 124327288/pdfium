{
  'variables': {
    # TODO(thakis): Enable this, pdfium:29
    #'chromium_code': 1,
    'pdf_use_skia%': 0,
    'pdf_enable_v8%': 1,
    'conditions': [
      ['OS=="linux"', {
        'bundle_freetype%': 0,
      }, {  # On Android there's no system FreeType. On Windows and Mac, only a
            # few methods are used from it.
        'bundle_freetype%': 1,
      }],
    ],
  },
  'target_defaults': {
    'defines' : [
      'OPJ_STATIC',
      'V8_DEPRECATION_WARNINGS',
      '_CRT_SECURE_NO_WARNINGS',
    ],
    'include_dirs': [
      'third_party/freetype/include',
    ],
    'conditions': [
      ['pdf_use_skia==1', {
        'defines': ['_SKIA_SUPPORT_'],
      }],
      ['pdf_enable_v8==1', {
        'defines': ['PDF_ENABLE_V8'],
      }],
      ['OS=="linux"', {
        'conditions': [
          ['target_arch=="x64"', {
            'defines' : [ '_FX_CPU_=_FX_X64_', ],
            'cflags': [ '-fPIC', ],
          }],
          ['target_arch=="ia32"', {
            'defines' : [ '_FX_CPU_=_FX_X86_', ],
          }],
        ],
      }],
    ],
    'msvs_disabled_warnings': [
      4005, 4018, 4146, 4333, 4345, 4267,
      # TODO(thestig): Fix all instances, remove this, pdfium:29
      4245, 4310, 4389, 4701, 4702, 4706, 4800,
    ],
    'variables': {
      'clang_warning_flags': [
        # TODO(thestig): Fix all instances, remove this, pdfium:29
        '-Wno-sign-compare',
      ],
      # Make sure Chromium's build/common.gypi doesn't re-add the flag on linux.
      'cflags_cc!': [ '-Wsign-compare' ],
    },
  },
  'targets': [
    {
      'target_name': 'pdfium',
      'type': 'static_library',
      'dependencies': [
        'third_party/third_party.gyp:bigint',
        'third_party/third_party.gyp:pdfium_base',
        'fdrm',
        'fpdfdoc',
        'fpdfapi',
        'fpdftext',
        'formfiller',
        'fxcodec',
        'fxcrt',
        'fxedit',
        'fxge',
        'javascript',
        'pdfwindow',
      ],
      'sources': [
        'fpdfsdk/include/fsdk_actionhandler.h',
        'fpdfsdk/include/fsdk_annothandler.h',
        'fpdfsdk/include/fsdk_baseannot.h',
        'fpdfsdk/include/fsdk_baseform.h',
        'fpdfsdk/src/fpdfdoc.cpp',
        'fpdfsdk/src/fpdfeditimg.cpp',
        'fpdfsdk/src/fpdfeditpage.cpp',
        'fpdfsdk/src/fpdfformfill.cpp',
        'fpdfsdk/src/fpdfppo.cpp',
        'fpdfsdk/src/fpdfsave.cpp',
        'fpdfsdk/src/fpdftext.cpp',
        'fpdfsdk/src/fpdfview.cpp',
        'fpdfsdk/src/fpdf_dataavail.cpp',
        'fpdfsdk/src/fpdf_ext.cpp',
        'fpdfsdk/src/fpdf_flatten.cpp',
        'fpdfsdk/src/fpdf_progressive.cpp',
        'fpdfsdk/src/fpdf_searchex.cpp',
        'fpdfsdk/src/fpdf_sysfontinfo.cpp',
        'fpdfsdk/src/fpdf_transformpage.cpp',
        'fpdfsdk/src/fsdk_actionhandler.cpp',
        'fpdfsdk/src/fsdk_annothandler.cpp',
        'fpdfsdk/src/fsdk_baseannot.cpp',
        'fpdfsdk/src/fsdk_baseform.cpp',
        'fpdfsdk/src/fsdk_mgr.cpp',
        'fpdfsdk/src/fsdk_rendercontext.cpp',
        'public/fpdf_dataavail.h',
        'public/fpdf_doc.h',
        'public/fpdf_edit.h',
        'public/fpdf_ext.h',
        'public/fpdf_flatten.h',
        'public/fpdf_formfill.h',
        'public/fpdf_fwlevent.h',
        'public/fpdf_ppo.h',
        'public/fpdf_progressive.h',
        'public/fpdf_save.h',
        'public/fpdf_searchex.h',
        'public/fpdf_sysfontinfo.h',
        'public/fpdf_text.h',
        'public/fpdf_transformpage.h',
        'public/fpdfview.h',
      ],
      'conditions': [
        ['bundle_freetype==1', {
          'dependencies': [
            'third_party/third_party.gyp:fx_freetype',
          ],
        }, {
          'link_settings': {
            'libraries': [
              '-lfreetype',
            ],
          },
        }],
      ],
      'all_dependent_settings': {
        'msvs_settings': {
          'VCLinkerTool': {
            'AdditionalDependencies': [
              'advapi32.lib',
              'gdi32.lib',
              'user32.lib',
            ],
          },
        },
        'conditions': [
          ['OS=="mac"', {
            'link_settings': {
              'libraries': [
                '$(SDKROOT)/System/Library/Frameworks/AppKit.framework',
                '$(SDKROOT)/System/Library/Frameworks/CoreFoundation.framework',
              ],
            },
          }],
        ],
      },
    },
    {
      'target_name': 'fdrm',
      'type': 'static_library',
      'sources': [
        'core/include/fdrm/fx_crypt.h',
        'core/src/fdrm/crypto/fx_crypt.cpp',
        'core/src/fdrm/crypto/fx_crypt_aes.cpp',
        'core/src/fdrm/crypto/fx_crypt_sha.cpp',
      ],
    },
    {
      'target_name': 'fpdfdoc',
      'type': 'static_library',
      'sources': [
        'core/include/fpdfdoc/fpdf_ap.h',
        'core/include/fpdfdoc/fpdf_doc.h',
        'core/include/fpdfdoc/fpdf_tagged.h',
        'core/include/fpdfdoc/fpdf_vt.h',
        'core/src/fpdfdoc/doc_action.cpp',
        'core/src/fpdfdoc/doc_annot.cpp',
        'core/src/fpdfdoc/doc_ap.cpp',
        'core/src/fpdfdoc/doc_basic.cpp',
        'core/src/fpdfdoc/doc_bookmark.cpp',
        'core/src/fpdfdoc/doc_form.cpp',
        'core/src/fpdfdoc/doc_formcontrol.cpp',
        'core/src/fpdfdoc/doc_formfield.cpp',
        'core/src/fpdfdoc/doc_link.cpp',
        'core/src/fpdfdoc/doc_metadata.cpp',
        'core/src/fpdfdoc/doc_ocg.cpp',
        'core/src/fpdfdoc/doc_tagged.cpp',
        'core/src/fpdfdoc/doc_utils.cpp',
        'core/src/fpdfdoc/doc_utils.h',
        'core/src/fpdfdoc/doc_viewerPreferences.cpp',
        'core/src/fpdfdoc/doc_vt.cpp',
        'core/src/fpdfdoc/doc_vtmodule.cpp',
        'core/src/fpdfdoc/pdf_vt.h',
        'core/src/fpdfdoc/tagged_int.h',
      ],
    },
    {
      'target_name': 'fpdfapi',
      'type': 'static_library',
      'sources': [
        'core/include/fpdfapi/fpdfapi.h',
        'core/include/fpdfapi/fpdf_module.h',
        'core/include/fpdfapi/fpdf_objects.h',
        'core/include/fpdfapi/fpdf_page.h',
        'core/include/fpdfapi/fpdf_pageobj.h',
        'core/include/fpdfapi/fpdf_parser.h',
        'core/include/fpdfapi/fpdf_render.h',
        'core/include/fpdfapi/fpdf_resource.h',
        'core/include/fpdfapi/fpdf_serial.h',
        'core/src/fpdfapi/fpdf_basic_module.cpp',
        'core/src/fpdfapi/fpdf_cmaps/cmap_int.h',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/Adobe-CNS1-UCS2_5.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/B5pc-H_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/B5pc-V_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/cmaps_cns1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/CNS-EUC-H_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/CNS-EUC-V_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/ETen-B5-H_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/ETen-B5-V_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/ETenms-B5-H_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/ETenms-B5-V_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/HKscs-B5-H_5.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/HKscs-B5-V_5.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/UniCNS-UCS2-H_3.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/UniCNS-UCS2-V_3.cpp',
        'core/src/fpdfapi/fpdf_cmaps/CNS1/UniCNS-UTF16-H_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/fpdf_cmaps.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/Adobe-GB1-UCS2_5.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/cmaps_gb1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/GB-EUC-H_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/GB-EUC-V_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/GBK-EUC-H_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/GBK-EUC-V_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/GBK2K-H_5.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/GBK2K-V_5.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/GBKp-EUC-H_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/GBKp-EUC-V_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/GBpc-EUC-H_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/GBpc-EUC-V_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/UniGB-UCS2-H_4.cpp',
        'core/src/fpdfapi/fpdf_cmaps/GB1/UniGB-UCS2-V_4.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/83pv-RKSJ-H_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/90ms-RKSJ-H_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/90ms-RKSJ-V_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/90msp-RKSJ-H_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/90msp-RKSJ-V_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/90pv-RKSJ-H_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/Add-RKSJ-H_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/Add-RKSJ-V_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/Adobe-Japan1-UCS2_4.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/cmaps_japan1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/EUC-H_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/EUC-V_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/Ext-RKSJ-H_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/Ext-RKSJ-V_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/H_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/UniJIS-UCS2-HW-H_4.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/UniJIS-UCS2-HW-V_4.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/UniJIS-UCS2-H_4.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/UniJIS-UCS2-V_4.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Japan1/V_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/Adobe-Korea1-UCS2_2.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/cmaps_korea1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/KSC-EUC-H_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/KSC-EUC-V_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/KSCms-UHC-HW-H_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/KSCms-UHC-HW-V_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/KSCms-UHC-H_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/KSCms-UHC-V_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/KSCpc-EUC-H_0.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/UniKS-UCS2-H_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/UniKS-UCS2-V_1.cpp',
        'core/src/fpdfapi/fpdf_cmaps/Korea1/UniKS-UTF16-H_0.cpp',
        'core/src/fpdfapi/fpdf_edit/editint.h',
        'core/src/fpdfapi/fpdf_edit/fpdf_edit_content.cpp',
        'core/src/fpdfapi/fpdf_edit/fpdf_edit_create.cpp',
        'core/src/fpdfapi/fpdf_edit/fpdf_edit_doc.cpp',
        'core/src/fpdfapi/fpdf_edit/fpdf_edit_image.cpp',
        'core/src/fpdfapi/fpdf_font/common.h',
        'core/src/fpdfapi/fpdf_font/font_int.h',
        'core/src/fpdfapi/fpdf_font/fpdf_font.cpp',
        'core/src/fpdfapi/fpdf_font/fpdf_font_charset.cpp',
        'core/src/fpdfapi/fpdf_font/fpdf_font_cid.cpp',
        'core/src/fpdfapi/fpdf_font/ttgsubtable.cpp',
        'core/src/fpdfapi/fpdf_font/ttgsubtable.h',
        'core/src/fpdfapi/fpdf_page/fpdf_page.cpp',
        'core/src/fpdfapi/fpdf_page/fpdf_page_colors.cpp',
        'core/src/fpdfapi/fpdf_page/fpdf_page_doc.cpp',
        'core/src/fpdfapi/fpdf_page/fpdf_page_func.cpp',
        'core/src/fpdfapi/fpdf_page/fpdf_page_graph_state.cpp',
        'core/src/fpdfapi/fpdf_page/fpdf_page_image.cpp',
        'core/src/fpdfapi/fpdf_page/fpdf_page_parser.cpp',
        'core/src/fpdfapi/fpdf_page/fpdf_page_parser_old.cpp',
        'core/src/fpdfapi/fpdf_page/fpdf_page_path.cpp',
        'core/src/fpdfapi/fpdf_page/fpdf_page_pattern.cpp',
        'core/src/fpdfapi/fpdf_page/pageint.h',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_decode.cpp',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_document.cpp',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_encrypt.cpp',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_fdf.cpp',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_objects.cpp',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_parser.cpp',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_utility.cpp',
        'core/src/fpdfapi/fpdf_parser/parser_int.h',
        'core/src/fpdfapi/fpdf_render/fpdf_render.cpp',
        'core/src/fpdfapi/fpdf_render/fpdf_render_cache.cpp',
        'core/src/fpdfapi/fpdf_render/fpdf_render_image.cpp',
        'core/src/fpdfapi/fpdf_render/fpdf_render_loadimage.cpp',
        'core/src/fpdfapi/fpdf_render/fpdf_render_pattern.cpp',
        'core/src/fpdfapi/fpdf_render/fpdf_render_text.cpp',
        'core/src/fpdfapi/fpdf_render/render_int.h',
      ],
    },
    {
      'target_name': 'fpdftext',
      'type': 'static_library',
      'sources': [
        'core/include/fpdftext/fpdf_text.h',
        'core/src/fpdftext/fpdf_text.cpp',
        'core/src/fpdftext/fpdf_text_int.cpp',
        'core/src/fpdftext/fpdf_text_search.cpp',
        'core/src/fpdftext/text_int.h',
        'core/src/fpdftext/txtproc.h',
        'core/src/fpdftext/unicodenormalization.cpp',
        'core/src/fpdftext/unicodenormalizationdata.cpp',
        'core/src/fpdftext/unicodenormalizationdata.h',
      ],
    },
    {
      'target_name': 'fxcodec',
      'type': 'static_library',
      'dependencies': [
        'third_party/third_party.gyp:fx_lcms2',
        'third_party/third_party.gyp:fx_libjpeg',
        'third_party/third_party.gyp:fx_libopenjpeg',
        'third_party/third_party.gyp:fx_zlib',
      ],
      'sources': [
        'core/include/fxcodec/fx_codec.h',
        'core/include/fxcodec/fx_codec_def.h',
        'core/include/fxcodec/fx_codec_flate.h',
        'core/src/fxcodec/codec/codec_int.h',
        'core/src/fxcodec/codec/fx_codec.cpp',
        'core/src/fxcodec/codec/fx_codec_fax.cpp',
        'core/src/fxcodec/codec/fx_codec_flate.cpp',
        'core/src/fxcodec/codec/fx_codec_icc.cpp',
        'core/src/fxcodec/codec/fx_codec_jbig.cpp',
        'core/src/fxcodec/codec/fx_codec_jbig_enc.cpp',
        'core/src/fxcodec/codec/fx_codec_jpeg.cpp',
        'core/src/fxcodec/codec/fx_codec_jpx_opj.cpp',
        'core/src/fxcodec/jbig2/JBig2_ArithDecoder.cpp',
        'core/src/fxcodec/jbig2/JBig2_ArithDecoder.h',
        'core/src/fxcodec/jbig2/JBig2_ArithIntDecoder.cpp',
        'core/src/fxcodec/jbig2/JBig2_ArithIntDecoder.h',
        'core/src/fxcodec/jbig2/JBig2_BitStream.cpp',
        'core/src/fxcodec/jbig2/JBig2_BitStream.h',
        'core/src/fxcodec/jbig2/JBig2_Context.cpp',
        'core/src/fxcodec/jbig2/JBig2_Context.h',
        'core/src/fxcodec/jbig2/JBig2_Define.h',
        'core/src/fxcodec/jbig2/JBig2_GrdProc.cpp',
        'core/src/fxcodec/jbig2/JBig2_GrdProc.h',
        'core/src/fxcodec/jbig2/JBig2_GrrdProc.cpp',
        'core/src/fxcodec/jbig2/JBig2_GrrdProc.h',
        'core/src/fxcodec/jbig2/JBig2_GsidProc.cpp',
        'core/src/fxcodec/jbig2/JBig2_GsidProc.h',
        'core/src/fxcodec/jbig2/JBig2_HtrdProc.cpp',
        'core/src/fxcodec/jbig2/JBig2_HtrdProc.h',
        'core/src/fxcodec/jbig2/JBig2_HuffmanDecoder.cpp',
        'core/src/fxcodec/jbig2/JBig2_HuffmanDecoder.h',
        'core/src/fxcodec/jbig2/JBig2_HuffmanTable.cpp',
        'core/src/fxcodec/jbig2/JBig2_HuffmanTable.h',
        'core/src/fxcodec/jbig2/JBig2_HuffmanTable_Standard.h',
        'core/src/fxcodec/jbig2/JBig2_Image.cpp',
        'core/src/fxcodec/jbig2/JBig2_Image.h',
        'core/src/fxcodec/jbig2/JBig2_List.h',
        'core/src/fxcodec/jbig2/JBig2_Page.h',
        'core/src/fxcodec/jbig2/JBig2_PatternDict.cpp',
        'core/src/fxcodec/jbig2/JBig2_PatternDict.h',
        'core/src/fxcodec/jbig2/JBig2_PddProc.cpp',
        'core/src/fxcodec/jbig2/JBig2_PddProc.h',
        'core/src/fxcodec/jbig2/JBig2_SddProc.cpp',
        'core/src/fxcodec/jbig2/JBig2_SddProc.h',
        'core/src/fxcodec/jbig2/JBig2_Segment.cpp',
        'core/src/fxcodec/jbig2/JBig2_Segment.h',
        'core/src/fxcodec/jbig2/JBig2_SymbolDict.cpp',
        'core/src/fxcodec/jbig2/JBig2_SymbolDict.h',
        'core/src/fxcodec/jbig2/JBig2_TrdProc.cpp',
        'core/src/fxcodec/jbig2/JBig2_TrdProc.h',
      ],
      'msvs_settings': {
        'VCCLCompilerTool': {
          # Unresolved warnings in fx_codec_jpx_opj.cpp
          # https://code.google.com/p/pdfium/issues/detail?id=100
          'WarnAsError': 'false',
        },
      },
      'conditions': [
        ['os_posix==1', {
          # core/src/fxcodec/fx_libopenjpeg/src/fx_mct.c does an pointer-to-int
          # conversion to check that an address is 16-bit aligned (benign).
          'cflags_c': [ '-Wno-pointer-to-int-cast' ],
        }],
      ],
    },
    {
      'target_name': 'fxcrt',
      'type': 'static_library',
      'sources': [
        'core/include/fxcrt/fx_basic.h',
        'core/include/fxcrt/fx_bidi.h',
        'core/include/fxcrt/fx_coordinates.h',
        'core/include/fxcrt/fx_ext.h',
        'core/include/fxcrt/fx_memory.h',
        'core/include/fxcrt/fx_safe_types.h',
        'core/include/fxcrt/fx_stream.h',
        'core/include/fxcrt/fx_string.h',
        'core/include/fxcrt/fx_system.h',
        'core/include/fxcrt/fx_ucd.h',
        'core/include/fxcrt/fx_xml.h',
        'core/src/fxcrt/extension.h',
        'core/src/fxcrt/fxcrt_platforms.cpp',
        'core/src/fxcrt/fxcrt_platforms.h',
        'core/src/fxcrt/fxcrt_posix.cpp',
        'core/src/fxcrt/fxcrt_posix.h',
        'core/src/fxcrt/fxcrt_windows.cpp',
        'core/src/fxcrt/fxcrt_windows.h',
        'core/src/fxcrt/fx_basic_array.cpp',
        'core/src/fxcrt/fx_basic_bstring.cpp',
        'core/src/fxcrt/fx_basic_buffer.cpp',
        'core/src/fxcrt/fx_basic_coords.cpp',
        'core/src/fxcrt/fx_basic_gcc.cpp',
        'core/src/fxcrt/fx_basic_list.cpp',
        'core/src/fxcrt/fx_basic_maps.cpp',
        'core/src/fxcrt/fx_basic_memmgr.cpp',
        'core/src/fxcrt/fx_basic_plex.cpp',
        'core/src/fxcrt/fx_basic_utf.cpp',
        'core/src/fxcrt/fx_basic_util.cpp',
        'core/src/fxcrt/fx_basic_wstring.cpp',
        'core/src/fxcrt/fx_bidi.cpp',
        'core/src/fxcrt/fx_extension.cpp',
        'core/src/fxcrt/fx_ucddata.cpp',
        'core/src/fxcrt/fx_unicode.cpp',
        'core/src/fxcrt/fx_xml_composer.cpp',
        'core/src/fxcrt/fx_xml_parser.cpp',
        'core/src/fxcrt/plex.h',
        'core/src/fxcrt/xml_int.h',
      ],
    },
    {
      'target_name': 'fxge',
      'type': 'static_library',
      'dependencies': [
        'third_party/third_party.gyp:fx_agg',
      ],
      'sources': [
        'core/include/fxge/fpf.h',
        'core/include/fxge/fx_dib.h',
        'core/include/fxge/fx_font.h',
        'core/include/fxge/fx_freetype.h',
        'core/include/fxge/fx_ge.h',
        'core/include/fxge/fx_ge_apple.h',
        'core/include/fxge/fx_ge_win32.h',
        'core/src/fxge/agg/include/fx_agg_driver.h',
        'core/src/fxge/agg/src/fx_agg_driver.cpp',
        'core/src/fxge/android/fpf_skiafont.cpp',
        'core/src/fxge/android/fpf_skiafont.h',
        'core/src/fxge/android/fpf_skiafontmgr.cpp',
        'core/src/fxge/android/fpf_skiafontmgr.h',
        'core/src/fxge/android/fpf_skiamodule.cpp',
        'core/src/fxge/android/fpf_skiamodule.h',
        'core/src/fxge/android/fx_android_font.cpp',
        'core/src/fxge/android/fx_android_font.h',
        'core/src/fxge/android/fx_android_imp.cpp',
        'core/src/fxge/android/fx_fpf.h',
        'core/src/fxge/apple/apple_int.h',
        'core/src/fxge/apple/fx_apple_platform.cpp',
        'core/src/fxge/apple/fx_mac_imp.cpp',
        'core/src/fxge/apple/fx_quartz_device.cpp',
        'core/src/fxge/dib/dib_int.h',
        'core/src/fxge/dib/fx_dib_composite.cpp',
        'core/src/fxge/dib/fx_dib_convert.cpp',
        'core/src/fxge/dib/fx_dib_engine.cpp',
        'core/src/fxge/dib/fx_dib_main.cpp',
        'core/src/fxge/dib/fx_dib_transform.cpp',
        'core/src/fxge/fontdata/chromefontdata/chromefontdata.h',
        'core/src/fxge/fontdata/chromefontdata/FoxitDingbats.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitFixed.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitFixedBold.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitFixedBoldItalic.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitFixedItalic.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSans.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSansBold.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSansBoldItalic.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSansItalic.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSansMM.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSerif.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSerifBold.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSerifBoldItalic.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSerifItalic.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSerifMM.c',
        'core/src/fxge/fontdata/chromefontdata/FoxitSymbol.c',
        'core/src/fxge/freetype/fx_freetype.c',
        'core/src/fxge/ge/fx_ge.cpp',
        'core/src/fxge/ge/fx_ge_device.cpp',
        'core/src/fxge/ge/fx_ge_font.cpp',
        'core/src/fxge/ge/fx_ge_fontmap.cpp',
        'core/src/fxge/ge/fx_ge_linux.cpp',
        'core/src/fxge/ge/fx_ge_path.cpp',
        'core/src/fxge/ge/fx_ge_ps.cpp',
        'core/src/fxge/ge/fx_ge_text.cpp',
        'core/src/fxge/ge/text_int.h',
      ],
      'variables': {
        'clang_warning_flags': [
          # http://code.google.com/p/pdfium/issues/detail?id=188
          '-Wno-switch',
        ],
      },
      'conditions': [
        ['pdf_use_skia==1', {
          'sources': [
            'core/src/fxge/skia/fx_skia_blitter_new.cpp',
            'core/src/fxge/skia/fx_skia_device.cpp',
          ],
          'dependencies': [
            '<(DEPTH)/skia/skia.gyp:skia',
          ],
          'include_dirs': [
            '<(DEPTH)/third_party/skia/include/config',
            '<(DEPTH)/third_party/skia/include/core',
            '<(DEPTH)/third_party/skia/include/effects',
            '<(DEPTH)/third_party/skia/include/images',
            '<(DEPTH)/third_party/skia/include/lazy',
            '<(DEPTH)/third_party/skia/include/pathops',
            '<(DEPTH)/third_party/skia/include/utils',
            '<(DEPTH)/third_party/skia/src/core',
          ],
        }],
        ['OS=="win"', {
          'defines!': [
            'WIN32_LEAN_AND_MEAN'
          ],
          'sources': [
            'core/src/fxge/win32/dwrite_int.h',
            'core/src/fxge/win32/fx_win32_device.cpp',
            'core/src/fxge/win32/fx_win32_dib.cpp',
            'core/src/fxge/win32/fx_win32_dwrite.cpp',
            'core/src/fxge/win32/fx_win32_gdipext.cpp',
            'core/src/fxge/win32/fx_win32_print.cpp',
            'core/src/fxge/win32/win32_int.h',
          ],
        }],
      ],
    },
    {
      'target_name': 'fxedit',
      'type': 'static_library',
      'sources': [
        'fpdfsdk/include/fxedit/fx_edit.h',
        'fpdfsdk/include/fxedit/fxet_edit.h',
        'fpdfsdk/include/fxedit/fxet_list.h',
        'fpdfsdk/include/fxedit/fxet_stub.h',
        'fpdfsdk/src/fxedit/fxet_ap.cpp',
        'fpdfsdk/src/fxedit/fxet_edit.cpp',
        'fpdfsdk/src/fxedit/fxet_list.cpp',
        'fpdfsdk/src/fxedit/fxet_module.cpp',
        'fpdfsdk/src/fxedit/fxet_pageobjs.cpp',
      ],
    },
    {
      'target_name': 'pdfwindow',
      'type': 'static_library',
      'sources': [
        'fpdfsdk/include/pdfwindow/IPDFWindow.h',
        'fpdfsdk/include/pdfwindow/PDFWindow.h',
        'fpdfsdk/include/pdfwindow/PWL_Button.h',
        'fpdfsdk/include/pdfwindow/PWL_Caret.h',
        'fpdfsdk/include/pdfwindow/PWL_ComboBox.h',
        'fpdfsdk/include/pdfwindow/PWL_Edit.h',
        'fpdfsdk/include/pdfwindow/PWL_EditCtrl.h',
        'fpdfsdk/include/pdfwindow/PWL_FontMap.h',
        'fpdfsdk/include/pdfwindow/PWL_Icon.h',
        'fpdfsdk/include/pdfwindow/PWL_IconList.h',
        'fpdfsdk/include/pdfwindow/PWL_Label.h',
        'fpdfsdk/include/pdfwindow/PWL_ListBox.h',
        'fpdfsdk/include/pdfwindow/PWL_ListCtrl.h',
        'fpdfsdk/include/pdfwindow/PWL_Note.h',
        'fpdfsdk/include/pdfwindow/PWL_ScrollBar.h',
        'fpdfsdk/include/pdfwindow/PWL_Signature.h',
        'fpdfsdk/include/pdfwindow/PWL_SpecialButton.h',
        'fpdfsdk/include/pdfwindow/PWL_Utils.h',
        'fpdfsdk/include/pdfwindow/PWL_Wnd.h',
        'fpdfsdk/src/pdfwindow/PWL_Button.cpp',
        'fpdfsdk/src/pdfwindow/PWL_Caret.cpp',
        'fpdfsdk/src/pdfwindow/PWL_ComboBox.cpp',
        'fpdfsdk/src/pdfwindow/PWL_Edit.cpp',
        'fpdfsdk/src/pdfwindow/PWL_EditCtrl.cpp',
        'fpdfsdk/src/pdfwindow/PWL_FontMap.cpp',
        'fpdfsdk/src/pdfwindow/PWL_Icon.cpp',
        'fpdfsdk/src/pdfwindow/PWL_IconList.cpp',
        'fpdfsdk/src/pdfwindow/PWL_Label.cpp',
        'fpdfsdk/src/pdfwindow/PWL_ListBox.cpp',
        'fpdfsdk/src/pdfwindow/PWL_ListCtrl.cpp',
        'fpdfsdk/src/pdfwindow/PWL_Note.cpp',
        'fpdfsdk/src/pdfwindow/PWL_ScrollBar.cpp',
        'fpdfsdk/src/pdfwindow/PWL_Signature.cpp',
        'fpdfsdk/src/pdfwindow/PWL_SpecialButton.cpp',
        'fpdfsdk/src/pdfwindow/PWL_Utils.cpp',
        'fpdfsdk/src/pdfwindow/PWL_Wnd.cpp',
      ],
    },
    {
      'target_name': 'javascript',
      'type': 'static_library',
      'sources': [
        'fpdfsdk/include/javascript/IJavaScript.h',
        'fpdfsdk/src/javascript/JS_Runtime_Stub.cpp',
      ],
      'conditions': [
        ['pdf_enable_v8==1', {
          'include_dirs': [
            '<(DEPTH)/v8',
            '<(DEPTH)/v8/include',
          ],
          'dependencies': [
            '<(DEPTH)/v8/tools/gyp/v8.gyp:v8',
          ],
          'export_dependent_settings': [
            '<(DEPTH)/v8/tools/gyp/v8.gyp:v8',
          ],
          'sources!': [
            'fpdfsdk/src/javascript/JS_Runtime_Stub.cpp',
          ],
          'sources': [
            'fpdfsdk/src/javascript/Consts.cpp',
            'fpdfsdk/src/javascript/Consts.h',
            'fpdfsdk/src/javascript/Document.cpp',
            'fpdfsdk/src/javascript/Document.h',
            'fpdfsdk/src/javascript/Field.cpp',
            'fpdfsdk/src/javascript/Field.h',
            'fpdfsdk/src/javascript/Icon.cpp',
            'fpdfsdk/src/javascript/Icon.h',
            'fpdfsdk/src/javascript/JS_Context.cpp',
            'fpdfsdk/src/javascript/JS_Context.h',
            'fpdfsdk/src/javascript/JS_Define.h',
            'fpdfsdk/src/javascript/JS_EventHandler.cpp',
            'fpdfsdk/src/javascript/JS_EventHandler.h',
            'fpdfsdk/src/javascript/JS_GlobalData.cpp',
            'fpdfsdk/src/javascript/JS_GlobalData.h',
            'fpdfsdk/src/javascript/JS_Object.cpp',
            'fpdfsdk/src/javascript/JS_Object.h',
            'fpdfsdk/src/javascript/JS_Runtime.cpp',
            'fpdfsdk/src/javascript/JS_Runtime.h',
            'fpdfsdk/src/javascript/JS_Value.cpp',
            'fpdfsdk/src/javascript/JS_Value.h',
            'fpdfsdk/src/javascript/PublicMethods.cpp',
            'fpdfsdk/src/javascript/PublicMethods.h',
            'fpdfsdk/src/javascript/app.cpp',
            'fpdfsdk/src/javascript/app.cpp',
            'fpdfsdk/src/javascript/app.h',
            'fpdfsdk/src/javascript/color.cpp',
            'fpdfsdk/src/javascript/color.cpp',
            'fpdfsdk/src/javascript/color.h',
            'fpdfsdk/src/javascript/console.cpp',
            'fpdfsdk/src/javascript/console.cpp',
            'fpdfsdk/src/javascript/console.h',
            'fpdfsdk/src/javascript/event.cpp',
            'fpdfsdk/src/javascript/event.h',
            'fpdfsdk/src/javascript/global.cpp',
            'fpdfsdk/src/javascript/global.h',
            'fpdfsdk/src/javascript/report.cpp',
            'fpdfsdk/src/javascript/report.h',
            'fpdfsdk/src/javascript/resource.cpp',
            'fpdfsdk/src/javascript/resource.h',
            'fpdfsdk/src/javascript/util.cpp',
            'fpdfsdk/src/javascript/util.h',
            'fpdfsdk/include/jsapi/fxjs_v8.h',
            'fpdfsdk/src/jsapi/fxjs_v8.cpp',
          ],
        }],
      ],
    },
    {
      'target_name': 'formfiller',
      'type': 'static_library',
      'sources': [
        'fpdfsdk/include/formfiller/FFL_CBA_Fontmap.h',
        'fpdfsdk/include/formfiller/FFL_CheckBox.h',
        'fpdfsdk/include/formfiller/FFL_ComboBox.h',
        'fpdfsdk/include/formfiller/FFL_FormFiller.h',
        'fpdfsdk/include/formfiller/FFL_IFormFiller.h',
        'fpdfsdk/include/formfiller/FFL_ListBox.h',
        'fpdfsdk/include/formfiller/FFL_PushButton.h',
        'fpdfsdk/include/formfiller/FFL_RadioButton.h',
        'fpdfsdk/include/formfiller/FFL_TextField.h',
        'fpdfsdk/include/formfiller/FormFiller.h',
        'fpdfsdk/src/formfiller/FFL_CBA_Fontmap.cpp',
        'fpdfsdk/src/formfiller/FFL_CheckBox.cpp',
        'fpdfsdk/src/formfiller/FFL_ComboBox.cpp',
        'fpdfsdk/src/formfiller/FFL_FormFiller.cpp',
        'fpdfsdk/src/formfiller/FFL_IFormFiller.cpp',
        'fpdfsdk/src/formfiller/FFL_ListBox.cpp',
        'fpdfsdk/src/formfiller/FFL_PushButton.cpp',
        'fpdfsdk/src/formfiller/FFL_RadioButton.cpp',
        'fpdfsdk/src/formfiller/FFL_TextField.cpp',
      ],
    },
    {
      'target_name': 'pdfium_unittests',
      'type': 'executable',
      'dependencies': [
        '<(DEPTH)/testing/gtest.gyp:gtest_main',
        '<(DEPTH)/testing/gtest.gyp:gtest',
        'pdfium',
        'test_support',
      ],
      'include_dirs': [
        '<(DEPTH)'
      ],
      'sources': [
        'core/src/fpdfapi/fpdf_font/fpdf_font_cid_unittest.cpp',
        'core/src/fpdfapi/fpdf_font/fpdf_font_unittest.cpp',
        'core/src/fpdfapi/fpdf_page/fpdf_page_parser_old_unittest.cpp',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_decode_unittest.cpp',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_parser_unittest.cpp',
        'core/src/fxcodec/codec/fx_codec_jpx_unittest.cpp',
        'core/src/fxcrt/fx_basic_bstring_unittest.cpp',
        'core/src/fxcrt/fx_basic_memmgr_unittest.cpp',
        'core/src/fxcrt/fx_basic_wstring_unittest.cpp',
        'core/src/fxcrt/fx_bidi_unittest.cpp',
        'core/src/fxcrt/fx_system_unittest.cpp',
        'testing/fx_string_testhelpers.h',
        'testing/fx_string_testhelpers.cpp',
        'third_party/base/nonstd_unique_ptr_unittest.cpp',
      ],
    },
    {
      'target_name': 'pdfium_embeddertests',
      'type': 'executable',
      'dependencies': [
        '<(DEPTH)/testing/gmock.gyp:gmock',
        '<(DEPTH)/testing/gtest.gyp:gtest',
        'pdfium',
        'test_support',
      ],
      'include_dirs': [
        '<(DEPTH)',
      ],
      'sources': [
        'core/src/fpdfapi/fpdf_page/fpdf_page_func_embeddertest.cpp',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_decode_embeddertest.cpp',
        'core/src/fpdfapi/fpdf_parser/fpdf_parser_parser_embeddertest.cpp',
        'core/src/fpdfapi/fpdf_render/fpdf_render_pattern_embeddertest.cpp',
        'fpdfsdk/src/fpdf_dataavail_embeddertest.cpp',
        'fpdfsdk/src/fpdfdoc_embeddertest.cpp',
        'fpdfsdk/src/fpdfformfill_embeddertest.cpp',
        'fpdfsdk/src/fpdftext_embeddertest.cpp',
        'fpdfsdk/src/fpdfview_c_api_test.c',
        'fpdfsdk/src/fpdfview_c_api_test.h',
        'fpdfsdk/src/fpdfview_embeddertest.cpp',
        'testing/embedder_test.cpp',
        'testing/embedder_test.h',
        'testing/embedder_test_mock_delegate.h',
        'testing/embedder_test_timer_handling_delegate.h',
      ],
      'conditions': [
        ['pdf_enable_v8==1', {
          'include_dirs': [
            '<(DEPTH)/v8',
            '<(DEPTH)/v8/include',
          ],
          'dependencies': [
            '<(DEPTH)/v8/tools/gyp/v8.gyp:v8',
            '<(DEPTH)/v8/tools/gyp/v8.gyp:v8_libplatform',
          ],
          'sources': [
            'fpdfsdk/src/jsapi/fxjs_v8_embeddertest.cpp',
          ],
        }],
      ],
    },
    {
      'target_name': 'test_support',
      'type': 'static_library',
      'dependencies': [
        '<(DEPTH)/testing/gmock.gyp:gmock',
        '<(DEPTH)/testing/gtest.gyp:gtest',
      ],
      'include_dirs': [
        '<(DEPTH)',
      ],
      'sources': [
        'testing/fx_string_testhelpers.cpp',
        'testing/fx_string_testhelpers.h',
        'testing/test_support.cpp',
        'testing/test_support.h',
      ],
      'conditions': [
        ['pdf_enable_v8==1', {
          'include_dirs': [
            '<(DEPTH)/v8',
            '<(DEPTH)/v8/include',
          ],
          'dependencies': [
            '<(DEPTH)/v8/tools/gyp/v8.gyp:v8',
            '<(DEPTH)/v8/tools/gyp/v8.gyp:v8_libplatform',
          ],
        }],
      ],
    },
  ],
}
