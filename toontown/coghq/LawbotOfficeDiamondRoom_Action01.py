# File: L (Python 2.4)

from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone13a',
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
    10074: {
        'type': 'attribModifier',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10000,
        'attribName': 'velocity',
        'recursive': 1,
        'typeName': 'goon',
        'value': '10.0' },
    10005: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 3.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'sg',
        'gridId': None,
        'hFov': 70,
        'strength': 15,
        'velocity': 10.0 },
    10011: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 3.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'sg',
        'gridId': None,
        'hFov': 70,
        'strength': 15,
        'velocity': 10.0 },
    10017: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 3.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'sg',
        'gridId': None,
        'hFov': 70,
        'strength': 15,
        'velocity': 10.0 },
    10022: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10018,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 3.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'sg',
        'gridId': None,
        'hFov': 70,
        'strength': 15,
        'velocity': 10.0 },
    10037: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10057,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(270, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam' },
    10039: {
        'type': 'model',
        'name': 'jumpCabinet',
        'comment': '',
        'parentEntId': 10057,
        'pos': Point3(0, 1.75, 0),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam' },
    10040: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10037,
        'pos': Point3(0, 0, 4),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam' },
    10041: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10057,
        'pos': Point3(0, 3.5, 0),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam' },
    10042: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10041,
        'pos': Point3(0, 0, 4),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam' },
    10043: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10052,
        'pos': Point3(1.95, -4, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam' },
    10044: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10051,
        'pos': Point3(1.95, 7, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam' },
    10045: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -7.7999999999999998, 0),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam' },
    10046: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -9.5999999999999996, 0),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam' },
    10047: {
        'type': 'model',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -11.4, 0),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam' },
    10048: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -7.7999999999999998, 4),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabB.bam' },
    10049: {
        'type': 'model',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -9.5999999999999996, 4),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam' },
    10050: {
        'type': 'model',
        'name': 'copy of <unnamed> (4)',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -11.4, 4),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabB.bam' },
    10056: {
        'type': 'model',
        'name': 'stepCrate',
        'comment': '',
        'parentEntId': 10053,
        'pos': Point3(-2.0869599999999999, 1.5294700000000001, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(0.40000000000000002, 0.40000000000000002, 0.40000000000000002),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_metal_crate.bam' },
    10059: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10062,
        'pos': Point3(-65.704300000000003, 26.772300000000001, 0),
        'hpr': Vec3(30.256399999999999, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam' },
    10060: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10062,
        'pos': Point3(-22.399699999999999, 48.329099999999997, 0),
        'hpr': Vec3(30.256399999999999, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam' },
    10061: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10062,
        'pos': Point3(-30.058599999999998, 11.8711, 0),
        'hpr': Vec3(30.256399999999999, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam' },
    10066: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10063,
        'pos': Point3(-35.553899999999999, -11.179500000000001, 0),
        'hpr': Vec3(326.31, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2.bam' },
    10067: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10063,
        'pos': Point3(-68.819599999999994, -28.184999999999999, 0),
        'hpr': Vec3(329.74000000000001, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam' },
    10068: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10063,
        'pos': Point3(-12.0298, -56.668199999999999, 0),
        'hpr': Vec3(326.31, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2.bam' },
    10069: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10065,
        'pos': Point3(37.402000000000001, -43.735900000000001, 0),
        'hpr': Vec3(33.689999999999998, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2.bam' },
    10070: {
        'type': 'model',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10065,
        'pos': Point3(23.282399999999999, -14.849600000000001, 0),
        'hpr': Vec3(28.610499999999998, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3.bam' },
    10071: {
        'type': 'model',
        'name': 'copy of <unnamed> (4)',
        'comment': '',
        'parentEntId': 10064,
        'pos': Point3(23.280000000000001, 14.85, 0),
        'hpr': Point3(-28.609999999999999, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3.bam' },
    10072: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10064,
        'pos': Point3(19.9879, 48.329099999999997, 0),
        'hpr': Point3(-30.260000000000002, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam' },
    10073: {
        'type': 'model',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10064,
        'pos': Point3(66.695700000000002, 25.769400000000001, 0),
        'hpr': Vec3(333.435, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam' },
    10075: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10063,
        'pos': Point3(-7.2733400000000001, -24.213200000000001, 0),
        'hpr': Vec3(326.31, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2.bam' },
    10076: {
        'type': 'model',
        'name': 'copy of <unnamed> (4)',
        'comment': '',
        'parentEntId': 10065,
        'pos': Point3(66.695700000000002, -29.136299999999999, 0),
        'hpr': Vec3(26.57, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam' },
    10000: {
        'type': 'nodepath',
        'name': 'goons',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10002: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(-74.931700000000006, -1.2693399999999999, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1) },
    10003: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0, -40.588000000000001, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1) },
    10004: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(-44.813299999999998, -38.389200000000002, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1) },
    10007: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(0, 30, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10008: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(-10, 40, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10009: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(-50, 10, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10010: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(-40, 30, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10013: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(15, -30, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10014: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(20, -45, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10015: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(40, -15, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10016: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(55, -30, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10019: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10018,
        'pos': Point3(20, 35, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10020: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10018,
        'pos': Point3(65, -10, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10021: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10018,
        'pos': Point3(55, 25, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10023: {
        'type': 'nodepath',
        'name': 'front',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-110, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10038: {
        'type': 'nodepath',
        'name': 'filingCabinetWall',
        'comment': '',
        'parentEntId': 10023,
        'pos': Point3(0, 1, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(2, 2, 2) },
    10051: {
        'type': 'nodepath',
        'name': 'leftCrate',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10052: {
        'type': 'nodepath',
        'name': 'rightCrate',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10053: {
        'type': 'nodepath',
        'name': 'leftCabinets',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10054: {
        'type': 'nodepath',
        'name': 'rightCabinets',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10057: {
        'type': 'nodepath',
        'name': 'cabinets',
        'comment': '',
        'parentEntId': 10053,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 1) },
    10058: {
        'type': 'nodepath',
        'name': 'obstacles',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10062: {
        'type': 'nodepath',
        'name': 'leftFront',
        'comment': '',
        'parentEntId': 10058,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10063: {
        'type': 'nodepath',
        'name': 'rightFront',
        'comment': '',
        'parentEntId': 10058,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10064: {
        'type': 'nodepath',
        'name': 'backLeft',
        'comment': '',
        'parentEntId': 10058,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10065: {
        'type': 'nodepath',
        'name': 'backRight',
        'comment': '',
        'parentEntId': 10058,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10001: {
        'type': 'pathMaster',
        'name': 'rightFrontGoon',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0,
        'pathTarget0': 10002,
        'pathTarget1': 10003,
        'pathTarget2': 10004,
        'pathTarget3': 0,
        'pathTarget4': 0,
        'pathTarget5': 0,
        'pathTarget6': 0,
        'pathTarget7': 0 },
    10006: {
        'type': 'pathMaster',
        'name': 'leftFrontGoon',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0,
        'pathTarget0': 10007,
        'pathTarget1': 10008,
        'pathTarget2': 10009,
        'pathTarget3': 10010,
        'pathTarget4': 0,
        'pathTarget5': 0,
        'pathTarget6': 0,
        'pathTarget7': 0 },
    10012: {
        'type': 'pathMaster',
        'name': 'rightRearGoon',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0,
        'pathTarget0': 10013,
        'pathTarget1': 10014,
        'pathTarget2': 10015,
        'pathTarget3': 10016,
        'pathTarget4': 0,
        'pathTarget5': 0,
        'pathTarget6': 0,
        'pathTarget7': 0 },
    10018: {
        'type': 'pathMaster',
        'name': 'leftRearGoon',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0,
        'pathTarget0': 10019,
        'pathTarget1': 10020,
        'pathTarget2': 10021,
        'pathTarget3': 0,
        'pathTarget4': 0,
        'pathTarget5': 0,
        'pathTarget6': 0,
        'pathTarget7': 0 } }
Scenario0 = { }
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0] }
