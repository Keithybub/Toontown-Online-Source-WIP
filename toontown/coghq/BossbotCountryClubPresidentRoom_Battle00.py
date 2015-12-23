# File: B (Python 2.4)

from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_12/models/bossbotHQ/BossbotPresidentsRm',
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
    110400: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(4, 0, 0),
        'hpr': Point3(270, 0, 0),
        'scale': Vec3(1, 1, 1),
        'cellId': 0,
        'radius': 10 },
    10002: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    110401: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(101.06999999999999, 0, 0),
        'hpr': Point3(270, 0, 0),
        'scale': Vec3(1, 1, 1) } }
Scenario0 = { }
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0] }
