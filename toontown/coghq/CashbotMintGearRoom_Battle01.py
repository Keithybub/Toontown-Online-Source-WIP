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
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE07a',
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
    10015: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10009,
        'pos': Point3(0.35536468029000001, 1.0326824188199999, 0.0),
        'hpr': Point3(99.459999084499998, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'gagLevel': 5,
        'gagLevelMax': 0,
        'gagTrack': 'random',
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 10 },
    10007: {
        'type': 'gear',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(2.0, -65.080001831100006, 11.0900001526),
        'hpr': Vec3(0.0, 90.0, 0.0),
        'scale': Point3(10.0, 10.0, 10.0),
        'degreesPerSec': 10.0,
        'gearScale': 1,
        'modelType': 'mint',
        'orientation': 'horizontal',
        'phaseShift': 0 },
    10008: {
        'type': 'gear',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-15.0, -65.080001831100006, 15.0),
        'hpr': Vec3(0.0, 90.0, 0.0),
        'scale': Point3(10.0, 10.0, 10.0),
        'degreesPerSec': -10.0,
        'gearScale': 1,
        'modelType': 'mint',
        'orientation': 'horizontal',
        'phaseShift': 0.26000000000000001 },
    10016: {
        'type': 'healBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10009,
        'pos': Point3(2.0886592865, -5.1962571144099998, 0.0),
        'hpr': Vec3(80.537681579600005, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 7,
        'rewardPerGrabMax': 10 },
    10001: {
        'type': 'locator',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'searchPath': '**/EXIT' },
    10012: {
        'type': 'mintProduct',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500 },
    10013: {
        'type': 'mintProduct',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(33.160278320300002, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500 },
    10014: {
        'type': 'mintProduct',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(0.0, -26.439891815199999, 0.0),
        'hpr': Vec3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500 },
    10002: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/VaultDoorCover.bam' },
    10004: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(28.420766830400002, 0.88671946525599998, 0.089056812226799995),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.4241015911099999, 1.4241015911099999, 1.4241015911099999),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_D.bam' },
    10005: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(1.02179563046, -5.7180581092800002, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(0.91270053386700001, 0.91270053386700001, 0.91270053386700001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_G1.bam' },
    10006: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(28.089681625400001, 6.6547060012800001, 0.069273389875899996),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_E.bam' },
    10010: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-30.341634750400001, -52.2014503479, 4.9408540725699996),
        'hpr': Vec3(180.0, 270.0, 270.0),
        'scale': Vec3(0.496759712696, 0.496759712696, 0.496759712696),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam' },
    10017: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-47.770233154300001, -15.772583961500001, 0.0),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(0.75, 0.75, 0.75),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam' },
    10000: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-16.258947372400002, 49.144668579099999, 10.288111686700001),
        'hpr': Vec3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10003: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10009: {
        'type': 'nodepath',
        'name': 'barrels',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(39.311466217000003, 1.0569336414299999, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10011: {
        'type': 'nodepath',
        'name': 'product',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-24.798507690400001, 59.846813201899998, 10.0710220337),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) } }
Scenario0 = { }
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0] }
