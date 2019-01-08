LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := kdaemonso
LOCAL_SRC_FILES := $(subst $(LOCAL_PATH)/,,$(wildcard $(LOCAL_PATH)/*.c))
LOCAL_C_INCLUDES += $(LOCAL_PATH)/
LOCAL_LDFLAGS += -pie -fPIC -fPIE -Wl,--gc-sections
LOCAL_CFLAGS += -std=c99 -pie -fPIC -fPIE -ffunction-sections -fdata-sections -fvisibility=hidden -DNDEBUG

include $(BUILD_EXECUTABLE)
