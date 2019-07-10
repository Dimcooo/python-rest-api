## Usage

All responses will have the form

```json
{
    "data": "Content for response",
    "message": "Description"
}
```

### List all Devices

**Definition**

`GET /Devices`

**Response**

```json
[
  {
    "identifier": "some-id",
    "name": "some-name",
    "device_type": "some-type",
    "controller_gateway": "192.168.0.1"
  },
  {
    "identifier": "some-other-id",
    "name": "some-other-name",
    "device_type": "some-other-type",
    "controller_gateway": "192.168.0.2"
  }
]
```

### Registering a new device

**Definition**

`POST /devices`

**Arguments**
— `"identifier":string a globally unique identifier for this device`
— `"name":string a friendly name for this device`
— `"device_type":string the type of the device as understood by the client`
— `"controller_gateway":string the IP address of the device's controller`
