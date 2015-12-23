# File: C (Python 2.4)

from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE08a',
        'wantDoors': 1 },
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None },
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': [] },
    10055: {
        'type': 'attribModifier',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'attribName': 'modelPath',
        'recursive': 1,
        'typeName': 'model',
        'value': '' },
    10045: {
        'type': 'gagBarrel',
        'name': 'gag',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(1.3697686195400001, 0.77302742004400005, 0.0),
        'hpr': Vec3(51.106670379599997, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'gagLevel': 5,
        'gagLevelMax': 0,
        'gagTrack': 'random',
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0 },
    10047: {
        'type': 'gagBarrel',
        'name': 'gag',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(0.137291625142, 2.8357563018800001, 0.0),
        'hpr': Vec3(-210.47303772000001, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'gagLevel': 5,
        'gagLevelMax': 0,
        'gagTrack': 'random',
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0 },
    10054: {
        'type': 'gagBarrel',
        'name': 'gag',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(-2.3486409187300001, 2.16795802116, 0.0),
        'hpr': Vec3(-141.715744019, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'gagLevel': 5,
        'gagLevelMax': 0,
        'gagTrack': 'random',
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0 },
    10020: {
        'type': 'gear',
        'name': 'upper',
        'comment': '',
        'parentEntId': 10044,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Point3(1.0, 1.0, 1.6000000238400001),
        'degreesPerSec': -5.0,
        'gearScale': 24.300000000000001,
        'modelType': 'mint',
        'orientation': 'horizontal',
        'phaseShift': 0 },
    10004: {
        'type': 'healBarrel',
        'name': 'heal',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(0.0, -0.74841457605399997, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 6,
        'rewardPerGrabMax': 8 },
    10005: {
        'type': 'healBarrel',
        'name': 'heal',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(-2.2019555568700002, -0.38430359959600002, 0.0),
        'hpr': Vec3(-64.431259155299998, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 6,
        'rewardPerGrabMax': 8 },
    10037: {
        'type': 'healBarrel',
        'name': 'atTheEnd',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(64.282081603999998, 42.8509597778, 0.0),
        'hpr': Vec3(274.90670776399998, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0 },
    10010: {
        'type': 'mintShelf',
        'name': 'shelf0',
        'comment': '',
        'parentEntId': 10023,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'mintId': 12700 },
    10021: {
        'type': 'mintShelf',
        'name': 'copy of shelf0',
        'comment': '',
        'parentEntId': 10023,
        'pos': Point3(-13.465435981800001, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Point3(1.0, 1.0, 1.0),
        'mintId': 12500 },
    10022: {
        'type': 'mintShelf',
        'name': 'copy of shelf0 (2)',
        'comment': '',
        'parentEntId': 10023,
        'pos': Point3(-26.882696151699999, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500 },
    10025: {
        'type': 'mintShelf',
        'name': 'shelf0',
        'comment': '',
        'parentEntId': 10024,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'mintId': 12500 },
    10026: {
        'type': 'mintShelf',
        'name': 'copy of shelf0',
        'comment': '',
        'parentEntId': 10024,
        'pos': Point3(-13.465435981800001, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500 },
    10027: {
        'type': 'mintShelf',
        'name': 'copy of shelf0 (2)',
        'comment': '',
        'parentEntId': 10024,
        'pos': Point3(-26.882696151699999, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500 },
    10000: {
        'type': 'model',
        'name': 'crate',
        'comment': '',
        'parentEntId': 10009,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10007: {
        'type': 'model',
        'name': 'upper',
        'comment': '',
        'parentEntId': 10059,
        'pos': Point3(0.0, 2.0, 5.5),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10008: {
        'type': 'model',
        'name': 'crate',
        'comment': '',
        'parentEntId': 10009,
        'pos': Point3(0.0, -5.7967944145199999, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10012: {
        'type': 'model',
        'name': 'copy of crate',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(0.0, -5.7967944145199999, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10013: {
        'type': 'model',
        'name': 'copy of crate (2)',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10014: {
        'type': 'model',
        'name': 'copy of crate (2)',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(-5.6528515815700002, -11.6494598389, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10015: {
        'type': 'model',
        'name': 'copy of crate (2)',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(-5.8057007789600004, -5.7967944145199999, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10016: {
        'type': 'model',
        'name': 'copy of crate (3)',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(-3.9382996559099999, -17.6477527618, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10018: {
        'type': 'model',
        'name': 'copy of upper',
        'comment': '',
        'parentEntId': 10059,
        'pos': Point3(0.0, -3.8336210250899998, 5.5),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10019: {
        'type': 'model',
        'name': 'copy of upper (2)',
        'comment': '',
        'parentEntId': 10059,
        'pos': Point3(0.0, -9.6930484771700005, 5.5),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10030: {
        'type': 'model',
        'name': 'lastCrateStack',
        'comment': '',
        'parentEntId': 10029,
        'pos': Point3(47.984870910600002, 27.710527419999998, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10031: {
        'type': 'model',
        'name': 'upper',
        'comment': '',
        'parentEntId': 10030,
        'pos': Point3(0.0, 0.0, 5.5),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10033: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10032,
        'pos': Point3(-41.869907379200001, -36.958232879599997, 0.0),
        'hpr': Point3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_D1.bam' },
    10034: {
        'type': 'model',
        'name': 'crateStack',
        'comment': '',
        'parentEntId': 10029,
        'pos': Point3(47.984870910600002, -3.0966691970800002, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10035: {
        'type': 'model',
        'name': 'upper',
        'comment': '',
        'parentEntId': 10034,
        'pos': Point3(0.0, 0.0, 5.5),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10036: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10032,
        'pos': Point3(0.0, -41.451602935799997, 30.268510818500001),
        'hpr': Vec3(180.0, 0.0, 180.0),
        'scale': Vec3(0.85034644603700005, 0.85034644603700005, 0.85034644603700005),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam' },
    10041: {
        'type': 'model',
        'name': 'crateStack',
        'comment': '',
        'parentEntId': 10040,
        'pos': Point3(36.590476989700001, -31.6758518219, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10042: {
        'type': 'model',
        'name': 'upper',
        'comment': '',
        'parentEntId': 10041,
        'pos': Point3(0.0, 0.0, 5.5),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10043: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10032,
        'pos': Point3(19.501714706400001, 84.078605651900006, 10.005873680100001),
        'hpr': Vec3(171.25384521500001, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/boiler_B1.bam' },
    10048: {
        'type': 'model',
        'name': 'crate',
        'comment': '',
        'parentEntId': 10046,
        'pos': Point3(0.0, 0.0, 8.25758934021),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Point3(1.2999999523200001, 1.2999999523200001, 1.6499999761599999),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10050: {
        'type': 'model',
        'name': 'support',
        'comment': '',
        'parentEntId': 10046,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/gears_C2.bam' },
    10052: {
        'type': 'model',
        'name': 'crate',
        'comment': '',
        'parentEntId': 10051,
        'pos': Point3(0.0, 0.0, 8.25758934021),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Point3(1.2999999523200001, 1.2999999523200001, 1.6499999761599999),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10053: {
        'type': 'model',
        'name': 'support',
        'comment': '',
        'parentEntId': 10051,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/gears_C2.bam' },
    10056: {
        'type': 'model',
        'name': 'collision',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(-0.62570387125000004, 0.82479703426399997, 0.0),
        'hpr': Vec3(318.366455078, 0.0, 0.0),
        'scale': Vec3(0.64461791515400002, 0.63999998569500005, 1.2872567176800001),
        'collisionsOnly': 1,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam' },
    10057: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10044,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(11.0614013672, 11.0614013672, 11.0614013672),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/RoundShadow.bam' },
    10058: {
        'type': 'model',
        'name': 'shelf',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(62.9968643188, 21.712474823000001, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/shelf_A1.bam' },
    10062: {
        'type': 'model',
        'name': 'copy of upper',
        'comment': '',
        'parentEntId': 10061,
        'pos': Point3(0.0, -3.8336210250899998, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10063: {
        'type': 'model',
        'name': 'copy of upper (2)',
        'comment': '',
        'parentEntId': 10061,
        'pos': Point3(0.0, -9.6930484771700005, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10064: {
        'type': 'model',
        'name': 'upper',
        'comment': '',
        'parentEntId': 10061,
        'pos': Point3(0.0, 2.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam' },
    10001: {
        'type': 'nodepath',
        'name': 'crates',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.2999999523200001, 1.2999999523200001, 1.6489242315299999) },
    10002: {
        'type': 'nodepath',
        'name': 'rewardBarrels',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-0.71973353624299996, 56.969058990500002, 10.0021047592),
        'hpr': Vec3(61.699245452900001, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10003: {
        'type': 'nodepath',
        'name': 'upperWall',
        'comment': 'TODO: replace with lines of shelves',
        'parentEntId': 0,
        'pos': Point3(-20.320251464799998, 52.654941558799997, 9.9087305068999996),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.1142984628699999, 1.1142984628699999, 1.1142984628699999) },
    10009: {
        'type': 'nodepath',
        'name': 'toGear0',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(-26.559331893900001, 31.855951309200002, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10011: {
        'type': 'nodepath',
        'name': 'toGear1',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(-25.883977890000001, 13.6748971939, 0.0),
        'hpr': Vec3(41.633541107200003, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10023: {
        'type': 'nodepath',
        'name': 'leftWall',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10024: {
        'type': 'nodepath',
        'name': 'rightWall',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-26.711175918599999, 6.8598155975299999, 0.0),
        'hpr': Point3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10028: {
        'type': 'nodepath',
        'name': 'lowerPuzzle',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.050000000745099998),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10029: {
        'type': 'nodepath',
        'name': 'entranceWall',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10032: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10038: {
        'type': 'nodepath',
        'name': 'archStompers',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10040: {
        'type': 'nodepath',
        'name': 'backWall',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10044: {
        'type': 'nodepath',
        'name': 'gear',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(11.850000381499999, -11.3800001144, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10046: {
        'type': 'nodepath',
        'name': 'supportedCrateBackWall',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(34.904460907000001, -34.058883667000003, -1.5168668031700001),
        'hpr': Vec3(63.434947967500001, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10051: {
        'type': 'nodepath',
        'name': 'supportedCrateEntrance',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(50.5076904298, 7.7591533660899996, 0.35789707303000001),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10059: {
        'type': 'nodepath',
        'name': 'largeStack',
        'comment': '',
        'parentEntId': 10029,
        'pos': Point3(47.979999542199998, -16.979999542200002, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10061: {
        'type': 'nodepath',
        'name': 'lower',
        'comment': '',
        'parentEntId': 10059,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10049: {
        'type': 'stomper',
        'name': 'second',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(62.368499755899997, -19.4456634521, 18.121715545699999),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'animateShadow': 1,
        'crushCellId': None,
        'damage': 8,
        'headScale': Point3(3.7999999523199999, 4.3000001907299996, 3.7999999523199999),
        'modelPath': 0,
        'motion': 3,
        'period': 3.0,
        'phaseShift': 0.34000000000000002,
        'range': 7.0,
        'removeCamBarrierCollisions': 0,
        'removeHeadFloor': 1,
        'shaftScale': Point3(1.71000003815, 2.78999996185, 1.71000003815),
        'soundLen': 0,
        'soundOn': 1,
        'soundPath': 1,
        'style': 'vertical',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 1,
        'zOffset': 0 } }
Scenario0 = { }
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0] }
