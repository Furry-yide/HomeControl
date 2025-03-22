# HomeControl
是一德家的智能家居更新仓库，其中主要是通过HTTPS进行通信。来控制家中全部已接入的设备

# 请求 request
```json5
{
  wantCtx: [
    "qq",
    "steam",
    "avatar",
    "someValue"
  ],
  commitData: {
    xxx: "xxx",
    xx1: 68463,
    xx2: "6LaK6L+H6ZW/5Z+O77yM6LWw5ZCR5LiW55WMCg==",
    Base64ed: [
      "xx2"
    ]
  }
}
```

# 响应 response

```json5
{
  // meta data
  metadata: {
    code: 1001,
    msg: "ok",
    // list all context
    contextTypes: {
      qq: "int",
      steam: "int",
      avatar: "bin,base64",
      someValue: "float,double"
    }
  },
  data: {
    qq: 10001,
    steam: 9726735,
    avatar: "6LaK6L+H6ZW/5Z+O77yM6LWw5ZCR5LiW55WMCg==",
    someValue: 86.32
  }
}
```