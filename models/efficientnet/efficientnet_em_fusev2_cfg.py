em_fusev2 = {
    'block_args': 
    [
        [
            {'block_type': 'er2', 'out_chs': 24, 'stride': 1, 'act_layer': None, 'exp_kernel_size': 3, 'pw_kernel_size': 1, 'exp_ratio': 4.0, 'force_in_chs': 24, 'se_ratio': 0.0, 'noskip': True}
            ], 
        [
            {'block_type': 'er2', 'out_chs': 32, 'stride': 2, 'act_layer': None, 'exp_kernel_size': 3, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'force_in_chs': 0, 'se_ratio': 0.0, 'noskip': False}, 
            {'block_type': 'er2', 'out_chs': 32, 'stride': 2, 'act_layer': None, 'exp_kernel_size': 3, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'force_in_chs': 0, 'se_ratio': 0.0, 'noskip': False}
            ], 
        [
            {'block_type': 'er2', 'out_chs': 48, 'stride': 2, 'act_layer': None, 'exp_kernel_size': 3, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'force_in_chs': 0, 'se_ratio': 0.0, 'noskip': False}, 
            {'block_type': 'er2', 'out_chs': 48, 'stride': 2, 'act_layer': None, 'exp_kernel_size': 3, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'force_in_chs': 0, 'se_ratio': 0.0, 'noskip': False}, 
            {'block_type': 'er2', 'out_chs': 48, 'stride': 2, 'act_layer': None, 'exp_kernel_size': 3, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'force_in_chs': 0, 'se_ratio': 0.0, 'noskip': False}, 
            {'block_type': 'er2', 'out_chs': 48, 'stride': 2, 'act_layer': None, 'exp_kernel_size': 3, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'force_in_chs': 0, 'se_ratio': 0.0, 'noskip': False}
            ], 
        [
            {'block_type': 'ir', 'out_chs': 96, 'stride': 2, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}, 
            {'block_type': 'ir', 'out_chs': 96, 'stride': 2, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}, 
            {'block_type': 'ir', 'out_chs': 96, 'stride': 2, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}, 
            {'block_type': 'ir', 'out_chs': 96, 'stride': 2, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}, 
            {'block_type': 'ir', 'out_chs': 96, 'stride': 2, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}
            ], 
        [
            {'block_type': 'ir', 'out_chs': 144, 'stride': 1, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}, 
            {'block_type': 'ir', 'out_chs': 144, 'stride': 1, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}, 
            {'block_type': 'ir', 'out_chs': 144, 'stride': 1, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}, 
            {'block_type': 'ir', 'out_chs': 144, 'stride': 1, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}
            ], 
        [
            {'block_type': 'ir', 'out_chs': 192, 'stride': 2, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}, 
            {'block_type': 'ir', 'out_chs': 192, 'stride': 2, 'act_layer': None, 'dw_kernel_size': 5, 'exp_kernel_size': 1, 'pw_kernel_size': 1, 'exp_ratio': 8.0, 'se_ratio': 0.0, 'noskip': False, 's2d': False}
            ]
        ], 
        'num_features': 1280, 
        'stem_size': 32, 
        'round_chs_fn': functools.partial(<function round_channels at 0x7fe3dcdd3af0>, multiplier=1.0), 
        'norm_layer': functools.partial(<class 'torch.nn.modules.batchnorm.BatchNorm2d'>), 
        'act_layer': <class 'torch.nn.modules.activation.ReLU'>
    }