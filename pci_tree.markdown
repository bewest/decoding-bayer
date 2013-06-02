## tree /sys/devices/pci0000\:00/
```
/sys/devices/pci0000:00/
├── 0000:00:00.0
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/agpgart-intel
│   ├── enable
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   └── runtime_usage
│   ├── remove
│   ├── rescan
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:01.0
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:00
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:01
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:01.0
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   └── runtime_usage
│   ├── remove
│   ├── rescan
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:07.0
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:01
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   └── runtime_usage
│   ├── remove
│   ├── rescan
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:07.1
│   ├── ata1
│   │   ├── ata_port
│   │   │   └── ata1
│   │   │       ├── device -> ../../../ata1
│   │   │       ├── idle_irq
│   │   │       ├── nr_pmp_links
│   │   │       ├── power
│   │   │       │   ├── async
│   │   │       │   ├── autosuspend_delay_ms
│   │   │       │   ├── control
│   │   │       │   ├── runtime_active_kids
│   │   │       │   ├── runtime_active_time
│   │   │       │   ├── runtime_enabled
│   │   │       │   ├── runtime_status
│   │   │       │   ├── runtime_suspended_time
│   │   │       │   └── runtime_usage
│   │   │       ├── subsystem -> ../../../../../../class/ata_port
│   │   │       └── uevent
│   │   ├── link1
│   │   │   ├── ata_link
│   │   │   │   └── link1
│   │   │   │       ├── device -> ../../../link1
│   │   │   │       ├── hw_sata_spd_limit
│   │   │   │       ├── power
│   │   │   │       │   ├── async
│   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │       │   ├── control
│   │   │   │       │   ├── runtime_active_kids
│   │   │   │       │   ├── runtime_active_time
│   │   │   │       │   ├── runtime_enabled
│   │   │   │       │   ├── runtime_status
│   │   │   │       │   ├── runtime_suspended_time
│   │   │   │       │   └── runtime_usage
│   │   │   │       ├── sata_spd
│   │   │   │       ├── sata_spd_limit
│   │   │   │       ├── subsystem -> ../../../../../../../class/ata_link
│   │   │   │       └── uevent
│   │   │   ├── dev1.0
│   │   │   │   ├── ata_device
│   │   │   │   │   └── dev1.0
│   │   │   │   │       ├── class
│   │   │   │   │       ├── device -> ../../../dev1.0
│   │   │   │   │       ├── dma_mode
│   │   │   │   │       ├── ering
│   │   │   │   │       ├── gscr
│   │   │   │   │       ├── id
│   │   │   │   │       ├── pio_mode
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── spdn_cnt
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/ata_device
│   │   │   │   │       ├── uevent
│   │   │   │   │       └── xfer_mode
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── control
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   └── uevent
│   │   │   ├── dev1.1
│   │   │   │   ├── ata_device
│   │   │   │   │   └── dev1.1
│   │   │   │   │       ├── class
│   │   │   │   │       ├── device -> ../../../dev1.1
│   │   │   │   │       ├── dma_mode
│   │   │   │   │       ├── ering
│   │   │   │   │       ├── gscr
│   │   │   │   │       ├── id
│   │   │   │   │       ├── pio_mode
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── spdn_cnt
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/ata_device
│   │   │   │   │       ├── uevent
│   │   │   │   │       └── xfer_mode
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── control
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   └── uevent
│   │   │   ├── power
│   │   │   │   ├── async
│   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   ├── control
│   │   │   │   ├── runtime_active_kids
│   │   │   │   ├── runtime_active_time
│   │   │   │   ├── runtime_enabled
│   │   │   │   ├── runtime_status
│   │   │   │   ├── runtime_suspended_time
│   │   │   │   └── runtime_usage
│   │   │   └── uevent
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   └── uevent
│   ├── ata2
│   │   ├── ata_port
│   │   │   └── ata2
│   │   │       ├── device -> ../../../ata2
│   │   │       ├── idle_irq
│   │   │       ├── nr_pmp_links
│   │   │       ├── power
│   │   │       │   ├── async
│   │   │       │   ├── autosuspend_delay_ms
│   │   │       │   ├── control
│   │   │       │   ├── runtime_active_kids
│   │   │       │   ├── runtime_active_time
│   │   │       │   ├── runtime_enabled
│   │   │       │   ├── runtime_status
│   │   │       │   ├── runtime_suspended_time
│   │   │       │   └── runtime_usage
│   │   │       ├── subsystem -> ../../../../../../class/ata_port
│   │   │       └── uevent
│   │   ├── link2
│   │   │   ├── ata_link
│   │   │   │   └── link2
│   │   │   │       ├── device -> ../../../link2
│   │   │   │       ├── hw_sata_spd_limit
│   │   │   │       ├── power
│   │   │   │       │   ├── async
│   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │       │   ├── control
│   │   │   │       │   ├── runtime_active_kids
│   │   │   │       │   ├── runtime_active_time
│   │   │   │       │   ├── runtime_enabled
│   │   │   │       │   ├── runtime_status
│   │   │   │       │   ├── runtime_suspended_time
│   │   │   │       │   └── runtime_usage
│   │   │   │       ├── sata_spd
│   │   │   │       ├── sata_spd_limit
│   │   │   │       ├── subsystem -> ../../../../../../../class/ata_link
│   │   │   │       └── uevent
│   │   │   ├── dev2.0
│   │   │   │   ├── ata_device
│   │   │   │   │   └── dev2.0
│   │   │   │   │       ├── class
│   │   │   │   │       ├── device -> ../../../dev2.0
│   │   │   │   │       ├── dma_mode
│   │   │   │   │       ├── ering
│   │   │   │   │       ├── gscr
│   │   │   │   │       ├── id
│   │   │   │   │       ├── pio_mode
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── spdn_cnt
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/ata_device
│   │   │   │   │       ├── uevent
│   │   │   │   │       └── xfer_mode
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── control
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   └── uevent
│   │   │   ├── dev2.1
│   │   │   │   ├── ata_device
│   │   │   │   │   └── dev2.1
│   │   │   │   │       ├── class
│   │   │   │   │       ├── device -> ../../../dev2.1
│   │   │   │   │       ├── dma_mode
│   │   │   │   │       ├── ering
│   │   │   │   │       ├── gscr
│   │   │   │   │       ├── id
│   │   │   │   │       ├── pio_mode
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── spdn_cnt
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/ata_device
│   │   │   │   │       ├── uevent
│   │   │   │   │       └── xfer_mode
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── control
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   └── uevent
│   │   │   ├── power
│   │   │   │   ├── async
│   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   ├── control
│   │   │   │   ├── runtime_active_kids
│   │   │   │   ├── runtime_active_time
│   │   │   │   ├── runtime_enabled
│   │   │   │   ├── runtime_status
│   │   │   │   ├── runtime_suspended_time
│   │   │   │   └── runtime_usage
│   │   │   └── uevent
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/ata_piix
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:04
│   ├── host0
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── scsi_host
│   │   │   └── host0
│   │   │       ├── active_mode
│   │   │       ├── can_queue
│   │   │       ├── cmd_per_lun
│   │   │       ├── device -> ../../../host0
│   │   │       ├── host_busy
│   │   │       ├── host_reset
│   │   │       ├── power
│   │   │       │   ├── async
│   │   │       │   ├── autosuspend_delay_ms
│   │   │       │   ├── control
│   │   │       │   ├── runtime_active_kids
│   │   │       │   ├── runtime_active_time
│   │   │       │   ├── runtime_enabled
│   │   │       │   ├── runtime_status
│   │   │       │   ├── runtime_suspended_time
│   │   │       │   └── runtime_usage
│   │   │       ├── proc_name
│   │   │       ├── prot_capabilities
│   │   │       ├── prot_guard_type
│   │   │       ├── scan
│   │   │       ├── sg_prot_tablesize
│   │   │       ├── sg_tablesize
│   │   │       ├── state
│   │   │       ├── subsystem -> ../../../../../../class/scsi_host
│   │   │       ├── supported_mode
│   │   │       ├── uevent
│   │   │       ├── unchecked_isa_dma
│   │   │       └── unique_id
│   │   ├── subsystem -> ../../../../bus/scsi
│   │   ├── target0:0:0
│   │   │   ├── 0:0:0:0
│   │   │   │   ├── block
│   │   │   │   │   └── sr0
│   │   │   │   │       ├── alignment_offset
│   │   │   │   │       ├── bdi -> ../../../../../../../virtual/bdi/11:0
│   │   │   │   │       ├── capability
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../0:0:0:0
│   │   │   │   │       ├── discard_alignment
│   │   │   │   │       ├── events
│   │   │   │   │       ├── events_async
│   │   │   │   │       ├── events_poll_msecs
│   │   │   │   │       ├── ext_range
│   │   │   │   │       ├── holders
│   │   │   │   │       ├── inflight
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── queue
│   │   │   │   │       │   ├── add_random
│   │   │   │   │       │   ├── bsg -> ../../../bsg/0:0:0:0
│   │   │   │   │       │   ├── discard_granularity
│   │   │   │   │       │   ├── discard_max_bytes
│   │   │   │   │       │   ├── discard_zeroes_data
│   │   │   │   │       │   ├── hw_sector_size
│   │   │   │   │       │   ├── iosched
│   │   │   │   │       │   │   ├── back_seek_max
│   │   │   │   │       │   │   ├── back_seek_penalty
│   │   │   │   │       │   │   ├── fifo_expire_async
│   │   │   │   │       │   │   ├── fifo_expire_sync
│   │   │   │   │       │   │   ├── group_idle
│   │   │   │   │       │   │   ├── low_latency
│   │   │   │   │       │   │   ├── quantum
│   │   │   │   │       │   │   ├── slice_async
│   │   │   │   │       │   │   ├── slice_async_rq
│   │   │   │   │       │   │   ├── slice_idle
│   │   │   │   │       │   │   └── slice_sync
│   │   │   │   │       │   ├── iostats
│   │   │   │   │       │   ├── logical_block_size
│   │   │   │   │       │   ├── max_hw_sectors_kb
│   │   │   │   │       │   ├── max_integrity_segments
│   │   │   │   │       │   ├── max_sectors_kb
│   │   │   │   │       │   ├── max_segments
│   │   │   │   │       │   ├── max_segment_size
│   │   │   │   │       │   ├── minimum_io_size
│   │   │   │   │       │   ├── nomerges
│   │   │   │   │       │   ├── nr_requests
│   │   │   │   │       │   ├── optimal_io_size
│   │   │   │   │       │   ├── physical_block_size
│   │   │   │   │       │   ├── read_ahead_kb
│   │   │   │   │       │   ├── rotational
│   │   │   │   │       │   ├── rq_affinity
│   │   │   │   │       │   └── scheduler
│   │   │   │   │       ├── range
│   │   │   │   │       ├── removable
│   │   │   │   │       ├── ro
│   │   │   │   │       ├── size
│   │   │   │   │       ├── slaves
│   │   │   │   │       ├── stat
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/block
│   │   │   │   │       ├── trace
│   │   │   │   │       │   ├── act_mask
│   │   │   │   │       │   ├── enable
│   │   │   │   │       │   ├── end_lba
│   │   │   │   │       │   ├── pid
│   │   │   │   │       │   └── start_lba
│   │   │   │   │       └── uevent
│   │   │   │   ├── bsg
│   │   │   │   │   └── 0:0:0:0
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../0:0:0:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/bsg
│   │   │   │   │       └── uevent
│   │   │   │   ├── delete
│   │   │   │   ├── device_blocked
│   │   │   │   ├── dh_state
│   │   │   │   ├── driver -> ../../../../../../bus/scsi/drivers/sr
│   │   │   │   ├── evt_media_change
│   │   │   │   ├── generic -> scsi_generic/sg0
│   │   │   │   ├── iocounterbits
│   │   │   │   ├── iodone_cnt
│   │   │   │   ├── ioerr_cnt
│   │   │   │   ├── iorequest_cnt
│   │   │   │   ├── modalias
│   │   │   │   ├── model
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── control
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   ├── queue_depth
│   │   │   │   ├── queue_type
│   │   │   │   ├── rescan
│   │   │   │   ├── rev
│   │   │   │   ├── scsi_device
│   │   │   │   │   └── 0:0:0:0
│   │   │   │   │       ├── device -> ../../../0:0:0:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/scsi_device
│   │   │   │   │       └── uevent
│   │   │   │   ├── scsi_generic
│   │   │   │   │   └── sg0
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../0:0:0:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/scsi_generic
│   │   │   │   │       └── uevent
│   │   │   │   ├── scsi_level
│   │   │   │   ├── state
│   │   │   │   ├── subsystem -> ../../../../../../bus/scsi
│   │   │   │   ├── timeout
│   │   │   │   ├── type
│   │   │   │   ├── uevent
│   │   │   │   ├── unload_heads
│   │   │   │   └── vendor
│   │   │   ├── power
│   │   │   │   ├── async
│   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   ├── control
│   │   │   │   ├── runtime_active_kids
│   │   │   │   ├── runtime_active_time
│   │   │   │   ├── runtime_enabled
│   │   │   │   ├── runtime_status
│   │   │   │   ├── runtime_suspended_time
│   │   │   │   └── runtime_usage
│   │   │   ├── subsystem -> ../../../../../bus/scsi
│   │   │   └── uevent
│   │   └── uevent
│   ├── host1
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── scsi_host
│   │   │   └── host1
│   │   │       ├── active_mode
│   │   │       ├── can_queue
│   │   │       ├── cmd_per_lun
│   │   │       ├── device -> ../../../host1
│   │   │       ├── host_busy
│   │   │       ├── host_reset
│   │   │       ├── power
│   │   │       │   ├── async
│   │   │       │   ├── autosuspend_delay_ms
│   │   │       │   ├── control
│   │   │       │   ├── runtime_active_kids
│   │   │       │   ├── runtime_active_time
│   │   │       │   ├── runtime_enabled
│   │   │       │   ├── runtime_status
│   │   │       │   ├── runtime_suspended_time
│   │   │       │   └── runtime_usage
│   │   │       ├── proc_name
│   │   │       ├── prot_capabilities
│   │   │       ├── prot_guard_type
│   │   │       ├── scan
│   │   │       ├── sg_prot_tablesize
│   │   │       ├── sg_tablesize
│   │   │       ├── state
│   │   │       ├── subsystem -> ../../../../../../class/scsi_host
│   │   │       ├── supported_mode
│   │   │       ├── uevent
│   │   │       ├── unchecked_isa_dma
│   │   │       └── unique_id
│   │   ├── subsystem -> ../../../../bus/scsi
│   │   ├── target1:0:0
│   │   │   ├── 1:0:0:0
│   │   │   │   ├── block
│   │   │   │   │   └── sr1
│   │   │   │   │       ├── alignment_offset
│   │   │   │   │       ├── bdi -> ../../../../../../../virtual/bdi/11:1
│   │   │   │   │       ├── capability
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../1:0:0:0
│   │   │   │   │       ├── discard_alignment
│   │   │   │   │       ├── events
│   │   │   │   │       ├── events_async
│   │   │   │   │       ├── events_poll_msecs
│   │   │   │   │       ├── ext_range
│   │   │   │   │       ├── holders
│   │   │   │   │       ├── inflight
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── queue
│   │   │   │   │       │   ├── add_random
│   │   │   │   │       │   ├── bsg -> ../../../bsg/1:0:0:0
│   │   │   │   │       │   ├── discard_granularity
│   │   │   │   │       │   ├── discard_max_bytes
│   │   │   │   │       │   ├── discard_zeroes_data
│   │   │   │   │       │   ├── hw_sector_size
│   │   │   │   │       │   ├── iosched
│   │   │   │   │       │   │   ├── back_seek_max
│   │   │   │   │       │   │   ├── back_seek_penalty
│   │   │   │   │       │   │   ├── fifo_expire_async
│   │   │   │   │       │   │   ├── fifo_expire_sync
│   │   │   │   │       │   │   ├── group_idle
│   │   │   │   │       │   │   ├── low_latency
│   │   │   │   │       │   │   ├── quantum
│   │   │   │   │       │   │   ├── slice_async
│   │   │   │   │       │   │   ├── slice_async_rq
│   │   │   │   │       │   │   ├── slice_idle
│   │   │   │   │       │   │   └── slice_sync
│   │   │   │   │       │   ├── iostats
│   │   │   │   │       │   ├── logical_block_size
│   │   │   │   │       │   ├── max_hw_sectors_kb
│   │   │   │   │       │   ├── max_integrity_segments
│   │   │   │   │       │   ├── max_sectors_kb
│   │   │   │   │       │   ├── max_segments
│   │   │   │   │       │   ├── max_segment_size
│   │   │   │   │       │   ├── minimum_io_size
│   │   │   │   │       │   ├── nomerges
│   │   │   │   │       │   ├── nr_requests
│   │   │   │   │       │   ├── optimal_io_size
│   │   │   │   │       │   ├── physical_block_size
│   │   │   │   │       │   ├── read_ahead_kb
│   │   │   │   │       │   ├── rotational
│   │   │   │   │       │   ├── rq_affinity
│   │   │   │   │       │   └── scheduler
│   │   │   │   │       ├── range
│   │   │   │   │       ├── removable
│   │   │   │   │       ├── ro
│   │   │   │   │       ├── size
│   │   │   │   │       ├── slaves
│   │   │   │   │       ├── stat
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/block
│   │   │   │   │       ├── trace
│   │   │   │   │       │   ├── act_mask
│   │   │   │   │       │   ├── enable
│   │   │   │   │       │   ├── end_lba
│   │   │   │   │       │   ├── pid
│   │   │   │   │       │   └── start_lba
│   │   │   │   │       └── uevent
│   │   │   │   ├── bsg
│   │   │   │   │   └── 1:0:0:0
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../1:0:0:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/bsg
│   │   │   │   │       └── uevent
│   │   │   │   ├── delete
│   │   │   │   ├── device_blocked
│   │   │   │   ├── dh_state
│   │   │   │   ├── driver -> ../../../../../../bus/scsi/drivers/sr
│   │   │   │   ├── evt_media_change
│   │   │   │   ├── generic -> scsi_generic/sg1
│   │   │   │   ├── iocounterbits
│   │   │   │   ├── iodone_cnt
│   │   │   │   ├── ioerr_cnt
│   │   │   │   ├── iorequest_cnt
│   │   │   │   ├── modalias
│   │   │   │   ├── model
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── control
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   ├── queue_depth
│   │   │   │   ├── queue_type
│   │   │   │   ├── rescan
│   │   │   │   ├── rev
│   │   │   │   ├── scsi_device
│   │   │   │   │   └── 1:0:0:0
│   │   │   │   │       ├── device -> ../../../1:0:0:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/scsi_device
│   │   │   │   │       └── uevent
│   │   │   │   ├── scsi_generic
│   │   │   │   │   └── sg1
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../1:0:0:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/scsi_generic
│   │   │   │   │       └── uevent
│   │   │   │   ├── scsi_level
│   │   │   │   ├── state
│   │   │   │   ├── subsystem -> ../../../../../../bus/scsi
│   │   │   │   ├── timeout
│   │   │   │   ├── type
│   │   │   │   ├── uevent
│   │   │   │   ├── unload_heads
│   │   │   │   └── vendor
│   │   │   ├── power
│   │   │   │   ├── async
│   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   ├── control
│   │   │   │   ├── runtime_active_kids
│   │   │   │   ├── runtime_active_time
│   │   │   │   ├── runtime_enabled
│   │   │   │   ├── runtime_status
│   │   │   │   ├── runtime_suspended_time
│   │   │   │   └── runtime_usage
│   │   │   ├── subsystem -> ../../../../../bus/scsi
│   │   │   └── uevent
│   │   └── uevent
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   └── runtime_usage
│   ├── remove
│   ├── rescan
│   ├── resource
│   ├── resource0
│   ├── resource1
│   ├── resource2
│   ├── resource3
│   ├── resource4
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:07.3
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:02
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   └── runtime_usage
│   ├── remove
│   ├── rescan
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:07.7
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/vmci
│   ├── enable
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   └── runtime_usage
│   ├── remove
│   ├── rescan
│   ├── resource
│   ├── resource0
│   ├── resource1
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:0f.0
│   ├── boot_vga
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/vmwgfx
│   ├── drm
│   │   ├── card0
│   │   │   ├── dev
│   │   │   ├── device -> ../../../0000:00:0f.0
│   │   │   ├── power
│   │   │   │   ├── async
│   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   ├── control
│   │   │   │   ├── runtime_active_kids
│   │   │   │   ├── runtime_active_time
│   │   │   │   ├── runtime_enabled
│   │   │   │   ├── runtime_status
│   │   │   │   ├── runtime_suspended_time
│   │   │   │   └── runtime_usage
│   │   │   ├── subsystem -> ../../../../../class/drm
│   │   │   └── uevent
│   │   └── controlD64
│   │       ├── dev
│   │       ├── device -> ../../../0000:00:0f.0
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── subsystem -> ../../../../../class/drm
│   │       └── uevent
│   ├── enable
│   ├── graphics
│   │   └── fb0
│   │       ├── bits_per_pixel
│   │       ├── blank
│   │       ├── bl_curve
│   │       ├── console
│   │       ├── cursor
│   │       ├── dev
│   │       ├── device -> ../../../0000:00:0f.0
│   │       ├── mode
│   │       ├── modes
│   │       ├── name
│   │       ├── pan
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rotate
│   │       ├── state
│   │       ├── stride
│   │       ├── subsystem -> ../../../../../class/graphics
│   │       ├── uevent
│   │       └── virtual_size
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   └── runtime_usage
│   ├── remove
│   ├── rescan
│   ├── resource
│   ├── resource0
│   ├── resource1
│   ├── resource1_wc
│   ├── resource2
│   ├── rom
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:10.0
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/mptspi
│   ├── enable
│   ├── host2
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── scsi_host
│   │   │   └── host2
│   │   │       ├── active_mode
│   │   │       ├── board_assembly
│   │   │       ├── board_name
│   │   │       ├── board_tracer
│   │   │       ├── can_queue
│   │   │       ├── cmd_per_lun
│   │   │       ├── debug_level
│   │   │       ├── device -> ../../../host2
│   │   │       ├── device_delay
│   │   │       ├── host_busy
│   │   │       ├── host_reset
│   │   │       ├── io_delay
│   │   │       ├── power
│   │   │       │   ├── async
│   │   │       │   ├── autosuspend_delay_ms
│   │   │       │   ├── control
│   │   │       │   ├── runtime_active_kids
│   │   │       │   ├── runtime_active_time
│   │   │       │   ├── runtime_enabled
│   │   │       │   ├── runtime_status
│   │   │       │   ├── runtime_suspended_time
│   │   │       │   └── runtime_usage
│   │   │       ├── proc_name
│   │   │       ├── prot_capabilities
│   │   │       ├── prot_guard_type
│   │   │       ├── scan
│   │   │       ├── sg_prot_tablesize
│   │   │       ├── sg_tablesize
│   │   │       ├── state
│   │   │       ├── subsystem -> ../../../../../../class/scsi_host
│   │   │       ├── supported_mode
│   │   │       ├── uevent
│   │   │       ├── unchecked_isa_dma
│   │   │       ├── unique_id
│   │   │       ├── version_bios
│   │   │       ├── version_fw
│   │   │       ├── version_mpi
│   │   │       ├── version_nvdata_default
│   │   │       ├── version_nvdata_persistent
│   │   │       └── version_product
│   │   ├── spi_host
│   │   │   └── host2
│   │   │       ├── device -> ../../../host2
│   │   │       ├── hba_id
│   │   │       ├── host_width
│   │   │       ├── power
│   │   │       │   ├── async
│   │   │       │   ├── autosuspend_delay_ms
│   │   │       │   ├── control
│   │   │       │   ├── runtime_active_kids
│   │   │       │   ├── runtime_active_time
│   │   │       │   ├── runtime_enabled
│   │   │       │   ├── runtime_status
│   │   │       │   ├── runtime_suspended_time
│   │   │       │   └── runtime_usage
│   │   │       ├── signalling
│   │   │       ├── subsystem -> ../../../../../../class/spi_host
│   │   │       └── uevent
│   │   ├── subsystem -> ../../../../bus/scsi
│   │   ├── target2:0:0
│   │   │   ├── 2:0:0:0
│   │   │   │   ├── block
│   │   │   │   │   └── sda
│   │   │   │   │       ├── alignment_offset
│   │   │   │   │       ├── bdi -> ../../../../../../../virtual/bdi/8:0
│   │   │   │   │       ├── capability
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../2:0:0:0
│   │   │   │   │       ├── discard_alignment
│   │   │   │   │       ├── events
│   │   │   │   │       ├── events_async
│   │   │   │   │       ├── events_poll_msecs
│   │   │   │   │       ├── ext_range
│   │   │   │   │       ├── holders
│   │   │   │   │       ├── inflight
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── queue
│   │   │   │   │       │   ├── add_random
│   │   │   │   │       │   ├── discard_granularity
│   │   │   │   │       │   ├── discard_max_bytes
│   │   │   │   │       │   ├── discard_zeroes_data
│   │   │   │   │       │   ├── hw_sector_size
│   │   │   │   │       │   ├── iosched
│   │   │   │   │       │   │   ├── back_seek_max
│   │   │   │   │       │   │   ├── back_seek_penalty
│   │   │   │   │       │   │   ├── fifo_expire_async
│   │   │   │   │       │   │   ├── fifo_expire_sync
│   │   │   │   │       │   │   ├── group_idle
│   │   │   │   │       │   │   ├── low_latency
│   │   │   │   │       │   │   ├── quantum
│   │   │   │   │       │   │   ├── slice_async
│   │   │   │   │       │   │   ├── slice_async_rq
│   │   │   │   │       │   │   ├── slice_idle
│   │   │   │   │       │   │   └── slice_sync
│   │   │   │   │       │   ├── iostats
│   │   │   │   │       │   ├── logical_block_size
│   │   │   │   │       │   ├── max_hw_sectors_kb
│   │   │   │   │       │   ├── max_integrity_segments
│   │   │   │   │       │   ├── max_sectors_kb
│   │   │   │   │       │   ├── max_segments
│   │   │   │   │       │   ├── max_segment_size
│   │   │   │   │       │   ├── minimum_io_size
│   │   │   │   │       │   ├── nomerges
│   │   │   │   │       │   ├── nr_requests
│   │   │   │   │       │   ├── optimal_io_size
│   │   │   │   │       │   ├── physical_block_size
│   │   │   │   │       │   ├── read_ahead_kb
│   │   │   │   │       │   ├── rotational
│   │   │   │   │       │   ├── rq_affinity
│   │   │   │   │       │   └── scheduler
│   │   │   │   │       ├── range
│   │   │   │   │       ├── removable
│   │   │   │   │       ├── ro
│   │   │   │   │       ├── sda1
│   │   │   │   │       │   ├── alignment_offset
│   │   │   │   │       │   ├── dev
│   │   │   │   │       │   ├── discard_alignment
│   │   │   │   │       │   ├── holders
│   │   │   │   │       │   ├── inflight
│   │   │   │   │       │   ├── partition
│   │   │   │   │       │   ├── power
│   │   │   │   │       │   │   ├── async
│   │   │   │   │       │   │   ├── autosuspend_delay_ms
│   │   │   │   │       │   │   ├── control
│   │   │   │   │       │   │   ├── runtime_active_kids
│   │   │   │   │       │   │   ├── runtime_active_time
│   │   │   │   │       │   │   ├── runtime_enabled
│   │   │   │   │       │   │   ├── runtime_status
│   │   │   │   │       │   │   ├── runtime_suspended_time
│   │   │   │   │       │   │   └── runtime_usage
│   │   │   │   │       │   ├── ro
│   │   │   │   │       │   ├── size
│   │   │   │   │       │   ├── start
│   │   │   │   │       │   ├── stat
│   │   │   │   │       │   ├── subsystem -> ../../../../../../../../../class/block
│   │   │   │   │       │   ├── trace
│   │   │   │   │       │   │   ├── act_mask
│   │   │   │   │       │   │   ├── enable
│   │   │   │   │       │   │   ├── end_lba
│   │   │   │   │       │   │   ├── pid
│   │   │   │   │       │   │   └── start_lba
│   │   │   │   │       │   └── uevent
│   │   │   │   │       ├── sda2
│   │   │   │   │       │   ├── alignment_offset
│   │   │   │   │       │   ├── dev
│   │   │   │   │       │   ├── discard_alignment
│   │   │   │   │       │   ├── holders
│   │   │   │   │       │   ├── inflight
│   │   │   │   │       │   ├── partition
│   │   │   │   │       │   ├── power
│   │   │   │   │       │   │   ├── async
│   │   │   │   │       │   │   ├── autosuspend_delay_ms
│   │   │   │   │       │   │   ├── control
│   │   │   │   │       │   │   ├── runtime_active_kids
│   │   │   │   │       │   │   ├── runtime_active_time
│   │   │   │   │       │   │   ├── runtime_enabled
│   │   │   │   │       │   │   ├── runtime_status
│   │   │   │   │       │   │   ├── runtime_suspended_time
│   │   │   │   │       │   │   └── runtime_usage
│   │   │   │   │       │   ├── ro
│   │   │   │   │       │   ├── size
│   │   │   │   │       │   ├── start
│   │   │   │   │       │   ├── stat
│   │   │   │   │       │   ├── subsystem -> ../../../../../../../../../class/block
│   │   │   │   │       │   ├── trace
│   │   │   │   │       │   │   ├── act_mask
│   │   │   │   │       │   │   ├── enable
│   │   │   │   │       │   │   ├── end_lba
│   │   │   │   │       │   │   ├── pid
│   │   │   │   │       │   │   └── start_lba
│   │   │   │   │       │   └── uevent
│   │   │   │   │       ├── sda5
│   │   │   │   │       │   ├── alignment_offset
│   │   │   │   │       │   ├── dev
│   │   │   │   │       │   ├── discard_alignment
│   │   │   │   │       │   ├── holders
│   │   │   │   │       │   ├── inflight
│   │   │   │   │       │   ├── partition
│   │   │   │   │       │   ├── power
│   │   │   │   │       │   │   ├── async
│   │   │   │   │       │   │   ├── autosuspend_delay_ms
│   │   │   │   │       │   │   ├── control
│   │   │   │   │       │   │   ├── runtime_active_kids
│   │   │   │   │       │   │   ├── runtime_active_time
│   │   │   │   │       │   │   ├── runtime_enabled
│   │   │   │   │       │   │   ├── runtime_status
│   │   │   │   │       │   │   ├── runtime_suspended_time
│   │   │   │   │       │   │   └── runtime_usage
│   │   │   │   │       │   ├── ro
│   │   │   │   │       │   ├── size
│   │   │   │   │       │   ├── start
│   │   │   │   │       │   ├── stat
│   │   │   │   │       │   ├── subsystem -> ../../../../../../../../../class/block
│   │   │   │   │       │   ├── trace
│   │   │   │   │       │   │   ├── act_mask
│   │   │   │   │       │   │   ├── enable
│   │   │   │   │       │   │   ├── end_lba
│   │   │   │   │       │   │   ├── pid
│   │   │   │   │       │   │   └── start_lba
│   │   │   │   │       │   └── uevent
│   │   │   │   │       ├── size
│   │   │   │   │       ├── slaves
│   │   │   │   │       ├── stat
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/block
│   │   │   │   │       ├── trace
│   │   │   │   │       │   ├── act_mask
│   │   │   │   │       │   ├── enable
│   │   │   │   │       │   ├── end_lba
│   │   │   │   │       │   ├── pid
│   │   │   │   │       │   └── start_lba
│   │   │   │   │       └── uevent
│   │   │   │   ├── bsg
│   │   │   │   │   └── 2:0:0:0
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../2:0:0:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/bsg
│   │   │   │   │       └── uevent
│   │   │   │   ├── delete
│   │   │   │   ├── device_blocked
│   │   │   │   ├── dh_state
│   │   │   │   ├── driver -> ../../../../../../bus/scsi/drivers/sd
│   │   │   │   ├── evt_media_change
│   │   │   │   ├── generic -> scsi_generic/sg2
│   │   │   │   ├── iocounterbits
│   │   │   │   ├── iodone_cnt
│   │   │   │   ├── ioerr_cnt
│   │   │   │   ├── iorequest_cnt
│   │   │   │   ├── modalias
│   │   │   │   ├── model
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── control
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   ├── queue_depth
│   │   │   │   ├── queue_ramp_up_period
│   │   │   │   ├── queue_type
│   │   │   │   ├── rescan
│   │   │   │   ├── rev
│   │   │   │   ├── scsi_device
│   │   │   │   │   └── 2:0:0:0
│   │   │   │   │       ├── device -> ../../../2:0:0:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/scsi_device
│   │   │   │   │       └── uevent
│   │   │   │   ├── scsi_disk
│   │   │   │   │   └── 2:0:0:0
│   │   │   │   │       ├── allow_restart
│   │   │   │   │       ├── app_tag_own
│   │   │   │   │       ├── cache_type
│   │   │   │   │       ├── device -> ../../../2:0:0:0
│   │   │   │   │       ├── FUA
│   │   │   │   │       ├── manage_start_stop
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── protection_mode
│   │   │   │   │       ├── protection_type
│   │   │   │   │       ├── provisioning_mode
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/scsi_disk
│   │   │   │   │       ├── thin_provisioning
│   │   │   │   │       └── uevent
│   │   │   │   ├── scsi_generic
│   │   │   │   │   └── sg2
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../2:0:0:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/scsi_generic
│   │   │   │   │       └── uevent
│   │   │   │   ├── scsi_level
│   │   │   │   ├── state
│   │   │   │   ├── subsystem -> ../../../../../../bus/scsi
│   │   │   │   ├── timeout
│   │   │   │   ├── type
│   │   │   │   ├── uevent
│   │   │   │   └── vendor
│   │   │   ├── power
│   │   │   │   ├── async
│   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   ├── control
│   │   │   │   ├── runtime_active_kids
│   │   │   │   ├── runtime_active_time
│   │   │   │   ├── runtime_enabled
│   │   │   │   ├── runtime_status
│   │   │   │   ├── runtime_suspended_time
│   │   │   │   └── runtime_usage
│   │   │   ├── spi_transport
│   │   │   │   └── target2:0:0
│   │   │   │       ├── device -> ../../../target2:0:0
│   │   │   │       ├── max_offset
│   │   │   │       ├── max_width
│   │   │   │       ├── min_period
│   │   │   │       ├── offset
│   │   │   │       ├── period
│   │   │   │       ├── power
│   │   │   │       │   ├── async
│   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │       │   ├── control
│   │   │   │       │   ├── runtime_active_kids
│   │   │   │       │   ├── runtime_active_time
│   │   │   │       │   ├── runtime_enabled
│   │   │   │       │   ├── runtime_status
│   │   │   │       │   ├── runtime_suspended_time
│   │   │   │       │   └── runtime_usage
│   │   │   │       ├── revalidate
│   │   │   │       ├── subsystem -> ../../../../../../../class/spi_transport
│   │   │   │       ├── uevent
│   │   │   │       └── width
│   │   │   ├── subsystem -> ../../../../../bus/scsi
│   │   │   └── uevent
│   │   ├── target2:0:1
│   │   │   ├── 2:0:1:0
│   │   │   │   ├── block
│   │   │   │   │   └── sdb
│   │   │   │   │       ├── alignment_offset
│   │   │   │   │       ├── bdi -> ../../../../../../../virtual/bdi/8:16
│   │   │   │   │       ├── capability
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../2:0:1:0
│   │   │   │   │       ├── discard_alignment
│   │   │   │   │       ├── events
│   │   │   │   │       ├── events_async
│   │   │   │   │       ├── events_poll_msecs
│   │   │   │   │       ├── ext_range
│   │   │   │   │       ├── holders
│   │   │   │   │       ├── inflight
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── queue
│   │   │   │   │       │   ├── add_random
│   │   │   │   │       │   ├── discard_granularity
│   │   │   │   │       │   ├── discard_max_bytes
│   │   │   │   │       │   ├── discard_zeroes_data
│   │   │   │   │       │   ├── hw_sector_size
│   │   │   │   │       │   ├── iosched
│   │   │   │   │       │   │   ├── back_seek_max
│   │   │   │   │       │   │   ├── back_seek_penalty
│   │   │   │   │       │   │   ├── fifo_expire_async
│   │   │   │   │       │   │   ├── fifo_expire_sync
│   │   │   │   │       │   │   ├── group_idle
│   │   │   │   │       │   │   ├── low_latency
│   │   │   │   │       │   │   ├── quantum
│   │   │   │   │       │   │   ├── slice_async
│   │   │   │   │       │   │   ├── slice_async_rq
│   │   │   │   │       │   │   ├── slice_idle
│   │   │   │   │       │   │   └── slice_sync
│   │   │   │   │       │   ├── iostats
│   │   │   │   │       │   ├── logical_block_size
│   │   │   │   │       │   ├── max_hw_sectors_kb
│   │   │   │   │       │   ├── max_integrity_segments
│   │   │   │   │       │   ├── max_sectors_kb
│   │   │   │   │       │   ├── max_segments
│   │   │   │   │       │   ├── max_segment_size
│   │   │   │   │       │   ├── minimum_io_size
│   │   │   │   │       │   ├── nomerges
│   │   │   │   │       │   ├── nr_requests
│   │   │   │   │       │   ├── optimal_io_size
│   │   │   │   │       │   ├── physical_block_size
│   │   │   │   │       │   ├── read_ahead_kb
│   │   │   │   │       │   ├── rotational
│   │   │   │   │       │   ├── rq_affinity
│   │   │   │   │       │   └── scheduler
│   │   │   │   │       ├── range
│   │   │   │   │       ├── removable
│   │   │   │   │       ├── ro
│   │   │   │   │       ├── sdb1
│   │   │   │   │       │   ├── alignment_offset
│   │   │   │   │       │   ├── dev
│   │   │   │   │       │   ├── discard_alignment
│   │   │   │   │       │   ├── holders
│   │   │   │   │       │   ├── inflight
│   │   │   │   │       │   ├── partition
│   │   │   │   │       │   ├── power
│   │   │   │   │       │   │   ├── async
│   │   │   │   │       │   │   ├── autosuspend_delay_ms
│   │   │   │   │       │   │   ├── control
│   │   │   │   │       │   │   ├── runtime_active_kids
│   │   │   │   │       │   │   ├── runtime_active_time
│   │   │   │   │       │   │   ├── runtime_enabled
│   │   │   │   │       │   │   ├── runtime_status
│   │   │   │   │       │   │   ├── runtime_suspended_time
│   │   │   │   │       │   │   └── runtime_usage
│   │   │   │   │       │   ├── ro
│   │   │   │   │       │   ├── size
│   │   │   │   │       │   ├── start
│   │   │   │   │       │   ├── stat
│   │   │   │   │       │   ├── subsystem -> ../../../../../../../../../class/block
│   │   │   │   │       │   ├── trace
│   │   │   │   │       │   │   ├── act_mask
│   │   │   │   │       │   │   ├── enable
│   │   │   │   │       │   │   ├── end_lba
│   │   │   │   │       │   │   ├── pid
│   │   │   │   │       │   │   └── start_lba
│   │   │   │   │       │   └── uevent
│   │   │   │   │       ├── size
│   │   │   │   │       ├── slaves
│   │   │   │   │       ├── stat
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/block
│   │   │   │   │       ├── trace
│   │   │   │   │       │   ├── act_mask
│   │   │   │   │       │   ├── enable
│   │   │   │   │       │   ├── end_lba
│   │   │   │   │       │   ├── pid
│   │   │   │   │       │   └── start_lba
│   │   │   │   │       └── uevent
│   │   │   │   ├── bsg
│   │   │   │   │   └── 2:0:1:0
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../2:0:1:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/bsg
│   │   │   │   │       └── uevent
│   │   │   │   ├── delete
│   │   │   │   ├── device_blocked
│   │   │   │   ├── dh_state
│   │   │   │   ├── driver -> ../../../../../../bus/scsi/drivers/sd
│   │   │   │   ├── evt_media_change
│   │   │   │   ├── generic -> scsi_generic/sg3
│   │   │   │   ├── iocounterbits
│   │   │   │   ├── iodone_cnt
│   │   │   │   ├── ioerr_cnt
│   │   │   │   ├── iorequest_cnt
│   │   │   │   ├── modalias
│   │   │   │   ├── model
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── control
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   ├── queue_depth
│   │   │   │   ├── queue_ramp_up_period
│   │   │   │   ├── queue_type
│   │   │   │   ├── rescan
│   │   │   │   ├── rev
│   │   │   │   ├── scsi_device
│   │   │   │   │   └── 2:0:1:0
│   │   │   │   │       ├── device -> ../../../2:0:1:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/scsi_device
│   │   │   │   │       └── uevent
│   │   │   │   ├── scsi_disk
│   │   │   │   │   └── 2:0:1:0
│   │   │   │   │       ├── allow_restart
│   │   │   │   │       ├── app_tag_own
│   │   │   │   │       ├── cache_type
│   │   │   │   │       ├── device -> ../../../2:0:1:0
│   │   │   │   │       ├── FUA
│   │   │   │   │       ├── manage_start_stop
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── protection_mode
│   │   │   │   │       ├── protection_type
│   │   │   │   │       ├── provisioning_mode
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/scsi_disk
│   │   │   │   │       ├── thin_provisioning
│   │   │   │   │       └── uevent
│   │   │   │   ├── scsi_generic
│   │   │   │   │   └── sg3
│   │   │   │   │       ├── dev
│   │   │   │   │       ├── device -> ../../../2:0:1:0
│   │   │   │   │       ├── power
│   │   │   │   │       │   ├── async
│   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │       │   ├── control
│   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │       │   ├── runtime_status
│   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │       │   └── runtime_usage
│   │   │   │   │       ├── subsystem -> ../../../../../../../../class/scsi_generic
│   │   │   │   │       └── uevent
│   │   │   │   ├── scsi_level
│   │   │   │   ├── state
│   │   │   │   ├── subsystem -> ../../../../../../bus/scsi
│   │   │   │   ├── timeout
│   │   │   │   ├── type
│   │   │   │   ├── uevent
│   │   │   │   └── vendor
│   │   │   ├── power
│   │   │   │   ├── async
│   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   ├── control
│   │   │   │   ├── runtime_active_kids
│   │   │   │   ├── runtime_active_time
│   │   │   │   ├── runtime_enabled
│   │   │   │   ├── runtime_status
│   │   │   │   ├── runtime_suspended_time
│   │   │   │   └── runtime_usage
│   │   │   ├── spi_transport
│   │   │   │   └── target2:0:1
│   │   │   │       ├── device -> ../../../target2:0:1
│   │   │   │       ├── max_offset
│   │   │   │       ├── max_width
│   │   │   │       ├── min_period
│   │   │   │       ├── offset
│   │   │   │       ├── period
│   │   │   │       ├── power
│   │   │   │       │   ├── async
│   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │       │   ├── control
│   │   │   │       │   ├── runtime_active_kids
│   │   │   │       │   ├── runtime_active_time
│   │   │   │       │   ├── runtime_enabled
│   │   │   │       │   ├── runtime_status
│   │   │   │       │   ├── runtime_suspended_time
│   │   │   │       │   └── runtime_usage
│   │   │   │       ├── revalidate
│   │   │   │       ├── subsystem -> ../../../../../../../class/spi_transport
│   │   │   │       ├── uevent
│   │   │   │       └── width
│   │   │   ├── subsystem -> ../../../../../bus/scsi
│   │   │   └── uevent
│   │   └── uevent
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   └── runtime_usage
│   ├── remove
│   ├── rescan
│   ├── resource
│   ├── resource0
│   ├── resource1
│   ├── resource3
│   ├── rom
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:11.0
│   ├── 0000:02:00.0
│   │   ├── broken_parity_status
│   │   ├── class
│   │   ├── config
│   │   ├── consistent_dma_mask_bits
│   │   ├── device
│   │   ├── dma_mask_bits
│   │   ├── driver -> ../../../../bus/pci/drivers/uhci_hcd
│   │   ├── enable
│   │   ├── firmware_node -> ../../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:05/device:06
│   │   ├── irq
│   │   ├── local_cpulist
│   │   ├── local_cpus
│   │   ├── modalias
│   │   ├── msi_bus
│   │   ├── numa_node
│   │   ├── pools
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   ├── runtime_usage
│   │   │   ├── wakeup
│   │   │   ├── wakeup_active
│   │   │   ├── wakeup_active_count
│   │   │   ├── wakeup_count
│   │   │   ├── wakeup_hit_count
│   │   │   ├── wakeup_last_time_ms
│   │   │   ├── wakeup_max_time_ms
│   │   │   └── wakeup_total_time_ms
│   │   ├── remove
│   │   ├── rescan
│   │   ├── resource
│   │   ├── resource4
│   │   ├── subsystem -> ../../../../bus/pci
│   │   ├── subsystem_device
│   │   ├── subsystem_vendor
│   │   ├── uevent
│   │   ├── usb2
│   │   │   ├── 2-0:1.0
│   │   │   │   ├── bAlternateSetting
│   │   │   │   ├── bInterfaceClass
│   │   │   │   ├── bInterfaceNumber
│   │   │   │   ├── bInterfaceProtocol
│   │   │   │   ├── bInterfaceSubClass
│   │   │   │   ├── bNumEndpoints
│   │   │   │   ├── driver -> ../../../../../../bus/usb/drivers/hub
│   │   │   │   ├── ep_81
│   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   ├── bInterval
│   │   │   │   │   ├── bLength
│   │   │   │   │   ├── bmAttributes
│   │   │   │   │   ├── direction
│   │   │   │   │   ├── interval
│   │   │   │   │   ├── power
│   │   │   │   │   │   ├── async
│   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   ├── control
│   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   ├── type
│   │   │   │   │   ├── uevent
│   │   │   │   │   └── wMaxPacketSize
│   │   │   │   ├── modalias
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   └── runtime_usage
│   │   │   │   ├── subsystem -> ../../../../../../bus/usb
│   │   │   │   ├── supports_autosuspend
│   │   │   │   └── uevent
│   │   │   ├── 2-1
│   │   │   │   ├── 2-1:1.0
│   │   │   │   │   ├── 0003:0E0F:0003.0001
│   │   │   │   │   │   ├── driver -> ../../../../../../../../bus/hid/drivers/generic-usb
│   │   │   │   │   │   ├── hidraw
│   │   │   │   │   │   │   └── hidraw0
│   │   │   │   │   │   │       ├── dev
│   │   │   │   │   │   │       ├── device -> ../../../0003:0E0F:0003.0001
│   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../class/hidraw
│   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── report_descriptor
│   │   │   │   │   │   ├── subsystem -> ../../../../../../../../bus/hid
│   │   │   │   │   │   └── uevent
│   │   │   │   │   ├── bAlternateSetting
│   │   │   │   │   ├── bInterfaceClass
│   │   │   │   │   ├── bInterfaceNumber
│   │   │   │   │   ├── bInterfaceProtocol
│   │   │   │   │   ├── bInterfaceSubClass
│   │   │   │   │   ├── bNumEndpoints
│   │   │   │   │   ├── driver -> ../../../../../../../bus/usb/drivers/usbhid
│   │   │   │   │   ├── ep_81
│   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   ├── direction
│   │   │   │   │   │   ├── interval
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── type
│   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   ├── input
│   │   │   │   │   │   └── input2
│   │   │   │   │   │       ├── capabilities
│   │   │   │   │   │       │   ├── abs
│   │   │   │   │   │       │   ├── ev
│   │   │   │   │   │       │   ├── ff
│   │   │   │   │   │       │   ├── key
│   │   │   │   │   │       │   ├── led
│   │   │   │   │   │       │   ├── msc
│   │   │   │   │   │       │   ├── rel
│   │   │   │   │   │       │   ├── snd
│   │   │   │   │   │       │   └── sw
│   │   │   │   │   │       ├── device -> ../../../2-1:1.0
│   │   │   │   │   │       ├── event2
│   │   │   │   │   │       │   ├── dev
│   │   │   │   │   │       │   ├── device -> ../../input2
│   │   │   │   │   │       │   ├── power
│   │   │   │   │   │       │   │   ├── async
│   │   │   │   │   │       │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │       │   │   ├── control
│   │   │   │   │   │       │   │   ├── runtime_active_kids
│   │   │   │   │   │       │   │   ├── runtime_active_time
│   │   │   │   │   │       │   │   ├── runtime_enabled
│   │   │   │   │   │       │   │   ├── runtime_status
│   │   │   │   │   │       │   │   ├── runtime_suspended_time
│   │   │   │   │   │       │   │   └── runtime_usage
│   │   │   │   │   │       │   ├── subsystem -> ../../../../../../../../../../class/input
│   │   │   │   │   │       │   └── uevent
│   │   │   │   │   │       ├── id
│   │   │   │   │   │       │   ├── bustype
│   │   │   │   │   │       │   ├── product
│   │   │   │   │   │       │   ├── vendor
│   │   │   │   │   │       │   └── version
│   │   │   │   │   │       ├── js0
│   │   │   │   │   │       │   ├── dev
│   │   │   │   │   │       │   ├── device -> ../../input2
│   │   │   │   │   │       │   ├── power
│   │   │   │   │   │       │   │   ├── async
│   │   │   │   │   │       │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │       │   │   ├── control
│   │   │   │   │   │       │   │   ├── runtime_active_kids
│   │   │   │   │   │       │   │   ├── runtime_active_time
│   │   │   │   │   │       │   │   ├── runtime_enabled
│   │   │   │   │   │       │   │   ├── runtime_status
│   │   │   │   │   │       │   │   ├── runtime_suspended_time
│   │   │   │   │   │       │   │   └── runtime_usage
│   │   │   │   │   │       │   ├── subsystem -> ../../../../../../../../../../class/input
│   │   │   │   │   │       │   └── uevent
│   │   │   │   │   │       ├── modalias
│   │   │   │   │   │       ├── mouse0
│   │   │   │   │   │       │   ├── dev
│   │   │   │   │   │       │   ├── device -> ../../input2
│   │   │   │   │   │       │   ├── power
│   │   │   │   │   │       │   │   ├── async
│   │   │   │   │   │       │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │       │   │   ├── control
│   │   │   │   │   │       │   │   ├── runtime_active_kids
│   │   │   │   │   │       │   │   ├── runtime_active_time
│   │   │   │   │   │       │   │   ├── runtime_enabled
│   │   │   │   │   │       │   │   ├── runtime_status
│   │   │   │   │   │       │   │   ├── runtime_suspended_time
│   │   │   │   │   │       │   │   └── runtime_usage
│   │   │   │   │   │       │   ├── subsystem -> ../../../../../../../../../../class/input
│   │   │   │   │   │       │   └── uevent
│   │   │   │   │   │       ├── name
│   │   │   │   │   │       ├── phys
│   │   │   │   │   │       ├── power
│   │   │   │   │   │       │   ├── async
│   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │       │   ├── control
│   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │       ├── properties
│   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../class/input
│   │   │   │   │   │       ├── uevent
│   │   │   │   │   │       └── uniq
│   │   │   │   │   ├── interface
│   │   │   │   │   ├── modalias
│   │   │   │   │   ├── power
│   │   │   │   │   │   ├── async
│   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   ├── subsystem -> ../../../../../../../bus/usb
│   │   │   │   │   ├── supports_autosuspend
│   │   │   │   │   └── uevent
│   │   │   │   ├── 2-1:1.1
│   │   │   │   │   ├── 0003:0E0F:0003.0002
│   │   │   │   │   │   ├── driver -> ../../../../../../../../bus/hid/drivers/generic-usb
│   │   │   │   │   │   ├── hidraw
│   │   │   │   │   │   │   └── hidraw1
│   │   │   │   │   │   │       ├── dev
│   │   │   │   │   │   │       ├── device -> ../../../0003:0E0F:0003.0002
│   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../class/hidraw
│   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── report_descriptor
│   │   │   │   │   │   ├── subsystem -> ../../../../../../../../bus/hid
│   │   │   │   │   │   └── uevent
│   │   │   │   │   ├── bAlternateSetting
│   │   │   │   │   ├── bInterfaceClass
│   │   │   │   │   ├── bInterfaceNumber
│   │   │   │   │   ├── bInterfaceProtocol
│   │   │   │   │   ├── bInterfaceSubClass
│   │   │   │   │   ├── bNumEndpoints
│   │   │   │   │   ├── driver -> ../../../../../../../bus/usb/drivers/usbhid
│   │   │   │   │   ├── ep_82
│   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   ├── direction
│   │   │   │   │   │   ├── interval
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── type
│   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   ├── input
│   │   │   │   │   │   └── input3
│   │   │   │   │   │       ├── capabilities
│   │   │   │   │   │       │   ├── abs
│   │   │   │   │   │       │   ├── ev
│   │   │   │   │   │       │   ├── ff
│   │   │   │   │   │       │   ├── key
│   │   │   │   │   │       │   ├── led
│   │   │   │   │   │       │   ├── msc
│   │   │   │   │   │       │   ├── rel
│   │   │   │   │   │       │   ├── snd
│   │   │   │   │   │       │   └── sw
│   │   │   │   │   │       ├── device -> ../../../2-1:1.1
│   │   │   │   │   │       ├── event3
│   │   │   │   │   │       │   ├── dev
│   │   │   │   │   │       │   ├── device -> ../../input3
│   │   │   │   │   │       │   ├── power
│   │   │   │   │   │       │   │   ├── async
│   │   │   │   │   │       │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │       │   │   ├── control
│   │   │   │   │   │       │   │   ├── runtime_active_kids
│   │   │   │   │   │       │   │   ├── runtime_active_time
│   │   │   │   │   │       │   │   ├── runtime_enabled
│   │   │   │   │   │       │   │   ├── runtime_status
│   │   │   │   │   │       │   │   ├── runtime_suspended_time
│   │   │   │   │   │       │   │   └── runtime_usage
│   │   │   │   │   │       │   ├── subsystem -> ../../../../../../../../../../class/input
│   │   │   │   │   │       │   └── uevent
│   │   │   │   │   │       ├── id
│   │   │   │   │   │       │   ├── bustype
│   │   │   │   │   │       │   ├── product
│   │   │   │   │   │       │   ├── vendor
│   │   │   │   │   │       │   └── version
│   │   │   │   │   │       ├── modalias
│   │   │   │   │   │       ├── mouse1
│   │   │   │   │   │       │   ├── dev
│   │   │   │   │   │       │   ├── device -> ../../input3
│   │   │   │   │   │       │   ├── power
│   │   │   │   │   │       │   │   ├── async
│   │   │   │   │   │       │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │       │   │   ├── control
│   │   │   │   │   │       │   │   ├── runtime_active_kids
│   │   │   │   │   │       │   │   ├── runtime_active_time
│   │   │   │   │   │       │   │   ├── runtime_enabled
│   │   │   │   │   │       │   │   ├── runtime_status
│   │   │   │   │   │       │   │   ├── runtime_suspended_time
│   │   │   │   │   │       │   │   └── runtime_usage
│   │   │   │   │   │       │   ├── subsystem -> ../../../../../../../../../../class/input
│   │   │   │   │   │       │   └── uevent
│   │   │   │   │   │       ├── name
│   │   │   │   │   │       ├── phys
│   │   │   │   │   │       ├── power
│   │   │   │   │   │       │   ├── async
│   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │       │   ├── control
│   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │       ├── properties
│   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../class/input
│   │   │   │   │   │       ├── uevent
│   │   │   │   │   │       └── uniq
│   │   │   │   │   ├── interface
│   │   │   │   │   ├── modalias
│   │   │   │   │   ├── power
│   │   │   │   │   │   ├── async
│   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   ├── subsystem -> ../../../../../../../bus/usb
│   │   │   │   │   ├── supports_autosuspend
│   │   │   │   │   └── uevent
│   │   │   │   ├── authorized
│   │   │   │   ├── avoid_reset_quirk
│   │   │   │   ├── bcdDevice
│   │   │   │   ├── bConfigurationValue
│   │   │   │   ├── bDeviceClass
│   │   │   │   ├── bDeviceProtocol
│   │   │   │   ├── bDeviceSubClass
│   │   │   │   ├── bmAttributes
│   │   │   │   ├── bMaxPacketSize0
│   │   │   │   ├── bMaxPower
│   │   │   │   ├── bNumConfigurations
│   │   │   │   ├── bNumInterfaces
│   │   │   │   ├── busnum
│   │   │   │   ├── configuration
│   │   │   │   ├── descriptors
│   │   │   │   ├── dev
│   │   │   │   ├── devnum
│   │   │   │   ├── devpath
│   │   │   │   ├── driver -> ../../../../../../bus/usb/drivers/usb
│   │   │   │   ├── ep_00
│   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   ├── bInterval
│   │   │   │   │   ├── bLength
│   │   │   │   │   ├── bmAttributes
│   │   │   │   │   ├── direction
│   │   │   │   │   ├── interval
│   │   │   │   │   ├── power
│   │   │   │   │   │   ├── async
│   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   ├── control
│   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   ├── type
│   │   │   │   │   ├── uevent
│   │   │   │   │   └── wMaxPacketSize
│   │   │   │   ├── idProduct
│   │   │   │   ├── idVendor
│   │   │   │   ├── manufacturer
│   │   │   │   ├── maxchild
│   │   │   │   ├── power
│   │   │   │   │   ├── active_duration
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── connected_duration
│   │   │   │   │   ├── control
│   │   │   │   │   ├── level
│   │   │   │   │   ├── persist
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   ├── product
│   │   │   │   ├── quirks
│   │   │   │   ├── remove
│   │   │   │   ├── speed
│   │   │   │   ├── subsystem -> ../../../../../../bus/usb
│   │   │   │   ├── uevent
│   │   │   │   ├── urbnum
│   │   │   │   └── version
│   │   │   ├── 2-2
│   │   │   │   ├── 2-2.1
│   │   │   │   │   ├── 2-2.1:1.0
│   │   │   │   │   │   ├── bAlternateSetting
│   │   │   │   │   │   ├── bInterfaceClass
│   │   │   │   │   │   ├── bInterfaceNumber
│   │   │   │   │   │   ├── bInterfaceProtocol
│   │   │   │   │   │   ├── bInterfaceSubClass
│   │   │   │   │   │   ├── bluetooth
│   │   │   │   │   │   │   └── hci0
│   │   │   │   │   │   │       ├── address
│   │   │   │   │   │   │       ├── bus
│   │   │   │   │   │   │       ├── class
│   │   │   │   │   │   │       ├── device -> ../../../2-2.1:1.0
│   │   │   │   │   │   │       ├── features
│   │   │   │   │   │   │       ├── hci_revision
│   │   │   │   │   │   │       ├── hci_version
│   │   │   │   │   │   │       ├── idle_timeout
│   │   │   │   │   │   │       ├── manufacturer
│   │   │   │   │   │   │       ├── name
│   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │       ├── rfkill0
│   │   │   │   │   │   │       │   ├── claim
│   │   │   │   │   │   │       │   ├── device -> ../../hci0
│   │   │   │   │   │   │       │   ├── hard
│   │   │   │   │   │   │       │   ├── index
│   │   │   │   │   │   │       │   ├── name
│   │   │   │   │   │   │       │   ├── persistent
│   │   │   │   │   │   │       │   ├── power
│   │   │   │   │   │   │       │   │   ├── async
│   │   │   │   │   │   │       │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │       │   │   ├── control
│   │   │   │   │   │   │       │   │   ├── runtime_active_kids
│   │   │   │   │   │   │       │   │   ├── runtime_active_time
│   │   │   │   │   │   │       │   │   ├── runtime_enabled
│   │   │   │   │   │   │       │   │   ├── runtime_status
│   │   │   │   │   │   │       │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │       │   │   └── runtime_usage
│   │   │   │   │   │   │       │   ├── soft
│   │   │   │   │   │   │       │   ├── state
│   │   │   │   │   │   │       │   ├── subsystem -> ../../../../../../../../../../../class/rfkill
│   │   │   │   │   │   │       │   ├── type
│   │   │   │   │   │   │       │   └── uevent
│   │   │   │   │   │   │       ├── sniff_max_interval
│   │   │   │   │   │   │       ├── sniff_min_interval
│   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../class/bluetooth
│   │   │   │   │   │   │       ├── type
│   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   ├── bNumEndpoints
│   │   │   │   │   │   ├── driver -> ../../../../../../../../bus/usb/drivers/btusb
│   │   │   │   │   │   ├── ep_02
│   │   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   │   ├── direction
│   │   │   │   │   │   │   ├── interval
│   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   │   ├── ep_81
│   │   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   │   ├── direction
│   │   │   │   │   │   │   ├── interval
│   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   │   ├── ep_82
│   │   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   │   ├── direction
│   │   │   │   │   │   │   ├── interval
│   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   │   ├── modalias
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── subsystem -> ../../../../../../../../bus/usb
│   │   │   │   │   │   ├── supports_autosuspend
│   │   │   │   │   │   └── uevent
│   │   │   │   │   ├── 2-2.1:1.1
│   │   │   │   │   │   ├── bAlternateSetting
│   │   │   │   │   │   ├── bInterfaceClass
│   │   │   │   │   │   ├── bInterfaceNumber
│   │   │   │   │   │   ├── bInterfaceProtocol
│   │   │   │   │   │   ├── bInterfaceSubClass
│   │   │   │   │   │   ├── bNumEndpoints
│   │   │   │   │   │   ├── driver -> ../../../../../../../../bus/usb/drivers/btusb
│   │   │   │   │   │   ├── ep_03
│   │   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   │   ├── direction
│   │   │   │   │   │   │   ├── interval
│   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   │   ├── ep_83
│   │   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   │   ├── direction
│   │   │   │   │   │   │   ├── interval
│   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   │   ├── modalias
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── subsystem -> ../../../../../../../../bus/usb
│   │   │   │   │   │   ├── supports_autosuspend
│   │   │   │   │   │   └── uevent
│   │   │   │   │   ├── authorized
│   │   │   │   │   ├── avoid_reset_quirk
│   │   │   │   │   ├── bcdDevice
│   │   │   │   │   ├── bConfigurationValue
│   │   │   │   │   ├── bDeviceClass
│   │   │   │   │   ├── bDeviceProtocol
│   │   │   │   │   ├── bDeviceSubClass
│   │   │   │   │   ├── bmAttributes
│   │   │   │   │   ├── bMaxPacketSize0
│   │   │   │   │   ├── bMaxPower
│   │   │   │   │   ├── bNumConfigurations
│   │   │   │   │   ├── bNumInterfaces
│   │   │   │   │   ├── busnum
│   │   │   │   │   ├── configuration
│   │   │   │   │   ├── descriptors
│   │   │   │   │   ├── dev
│   │   │   │   │   ├── devnum
│   │   │   │   │   ├── devpath
│   │   │   │   │   ├── driver -> ../../../../../../../bus/usb/drivers/usb
│   │   │   │   │   ├── ep_00
│   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   ├── direction
│   │   │   │   │   │   ├── interval
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── type
│   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   ├── idProduct
│   │   │   │   │   ├── idVendor
│   │   │   │   │   ├── manufacturer
│   │   │   │   │   ├── maxchild
│   │   │   │   │   ├── power
│   │   │   │   │   │   ├── active_duration
│   │   │   │   │   │   ├── async
│   │   │   │   │   │   ├── autosuspend
│   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   ├── connected_duration
│   │   │   │   │   │   ├── control
│   │   │   │   │   │   ├── level
│   │   │   │   │   │   ├── persist
│   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   ├── product
│   │   │   │   │   ├── quirks
│   │   │   │   │   ├── remove
│   │   │   │   │   ├── serial
│   │   │   │   │   ├── speed
│   │   │   │   │   ├── subsystem -> ../../../../../../../bus/usb
│   │   │   │   │   ├── uevent
│   │   │   │   │   ├── urbnum
│   │   │   │   │   └── version
│   │   │   │   ├── 2-2:1.0
│   │   │   │   │   ├── bAlternateSetting
│   │   │   │   │   ├── bInterfaceClass
│   │   │   │   │   ├── bInterfaceNumber
│   │   │   │   │   ├── bInterfaceProtocol
│   │   │   │   │   ├── bInterfaceSubClass
│   │   │   │   │   ├── bNumEndpoints
│   │   │   │   │   ├── driver -> ../../../../../../../bus/usb/drivers/hub
│   │   │   │   │   ├── ep_81
│   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   ├── direction
│   │   │   │   │   │   ├── interval
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── type
│   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   ├── interface
│   │   │   │   │   ├── modalias
│   │   │   │   │   ├── power
│   │   │   │   │   │   ├── async
│   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   ├── subsystem -> ../../../../../../../bus/usb
│   │   │   │   │   ├── supports_autosuspend
│   │   │   │   │   └── uevent
│   │   │   │   ├── 2-2.2
│   │   │   │   │   ├── 2-2.2:1.0
│   │   │   │   │   │   ├── bAlternateSetting
│   │   │   │   │   │   ├── bInterfaceClass
│   │   │   │   │   │   ├── bInterfaceNumber
│   │   │   │   │   │   ├── bInterfaceProtocol
│   │   │   │   │   │   ├── bInterfaceSubClass
│   │   │   │   │   │   ├── bNumEndpoints
│   │   │   │   │   │   ├── ep_01
│   │   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   │   ├── direction
│   │   │   │   │   │   │   ├── interval
│   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   │   ├── ep_81
│   │   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   │   ├── direction
│   │   │   │   │   │   │   ├── interval
│   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   │   ├── interface
│   │   │   │   │   │   ├── modalias
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── subsystem -> ../../../../../../../../bus/usb
│   │   │   │   │   │   ├── supports_autosuspend
│   │   │   │   │   │   └── uevent
│   │   │   │   │   ├── 2-2.2:1.1
│   │   │   │   │   │   ├── bAlternateSetting
│   │   │   │   │   │   ├── bInterfaceClass
│   │   │   │   │   │   ├── bInterfaceNumber
│   │   │   │   │   │   ├── bInterfaceProtocol
│   │   │   │   │   │   ├── bInterfaceSubClass
│   │   │   │   │   │   ├── bNumEndpoints
│   │   │   │   │   │   ├── driver -> ../../../../../../../../bus/usb/drivers/usb-storage
│   │   │   │   │   │   ├── ep_02
│   │   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   │   ├── direction
│   │   │   │   │   │   │   ├── interval
│   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   │   ├── ep_82
│   │   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   │   ├── direction
│   │   │   │   │   │   │   ├── interval
│   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   │   ├── host6
│   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   ├── scsi_host
│   │   │   │   │   │   │   │   └── host6
│   │   │   │   │   │   │   │       ├── active_mode
│   │   │   │   │   │   │   │       ├── can_queue
│   │   │   │   │   │   │   │       ├── cmd_per_lun
│   │   │   │   │   │   │   │       ├── device -> ../../../host6
│   │   │   │   │   │   │   │       ├── host_busy
│   │   │   │   │   │   │   │       ├── host_reset
│   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │       ├── proc_name
│   │   │   │   │   │   │   │       ├── prot_capabilities
│   │   │   │   │   │   │   │       ├── prot_guard_type
│   │   │   │   │   │   │   │       ├── scan
│   │   │   │   │   │   │   │       ├── sg_prot_tablesize
│   │   │   │   │   │   │   │       ├── sg_tablesize
│   │   │   │   │   │   │   │       ├── state
│   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../class/scsi_host
│   │   │   │   │   │   │   │       ├── supported_mode
│   │   │   │   │   │   │   │       ├── uevent
│   │   │   │   │   │   │   │       ├── unchecked_isa_dma
│   │   │   │   │   │   │   │       └── unique_id
│   │   │   │   │   │   │   ├── subsystem -> ../../../../../../../../../bus/scsi
│   │   │   │   │   │   │   ├── target6:0:0
│   │   │   │   │   │   │   │   ├── 6:0:0:0
│   │   │   │   │   │   │   │   │   ├── block
│   │   │   │   │   │   │   │   │   │   └── sdc
│   │   │   │   │   │   │   │   │   │       ├── alignment_offset
│   │   │   │   │   │   │   │   │   │       ├── bdi -> ../../../../../../../../../../../../virtual/bdi/8:32
│   │   │   │   │   │   │   │   │   │       ├── capability
│   │   │   │   │   │   │   │   │   │       ├── dev
│   │   │   │   │   │   │   │   │   │       ├── device -> ../../../6:0:0:0
│   │   │   │   │   │   │   │   │   │       ├── discard_alignment
│   │   │   │   │   │   │   │   │   │       ├── events
│   │   │   │   │   │   │   │   │   │       ├── events_async
│   │   │   │   │   │   │   │   │   │       ├── events_poll_msecs
│   │   │   │   │   │   │   │   │   │       ├── ext_range
│   │   │   │   │   │   │   │   │   │       ├── holders
│   │   │   │   │   │   │   │   │   │       ├── inflight
│   │   │   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │   │   │       ├── queue
│   │   │   │   │   │   │   │   │   │       │   ├── add_random
│   │   │   │   │   │   │   │   │   │       │   ├── discard_granularity
│   │   │   │   │   │   │   │   │   │       │   ├── discard_max_bytes
│   │   │   │   │   │   │   │   │   │       │   ├── discard_zeroes_data
│   │   │   │   │   │   │   │   │   │       │   ├── hw_sector_size
│   │   │   │   │   │   │   │   │   │       │   ├── iosched
│   │   │   │   │   │   │   │   │   │       │   │   ├── back_seek_max
│   │   │   │   │   │   │   │   │   │       │   │   ├── back_seek_penalty
│   │   │   │   │   │   │   │   │   │       │   │   ├── fifo_expire_async
│   │   │   │   │   │   │   │   │   │       │   │   ├── fifo_expire_sync
│   │   │   │   │   │   │   │   │   │       │   │   ├── group_idle
│   │   │   │   │   │   │   │   │   │       │   │   ├── low_latency
│   │   │   │   │   │   │   │   │   │       │   │   ├── quantum
│   │   │   │   │   │   │   │   │   │       │   │   ├── slice_async
│   │   │   │   │   │   │   │   │   │       │   │   ├── slice_async_rq
│   │   │   │   │   │   │   │   │   │       │   │   ├── slice_idle
│   │   │   │   │   │   │   │   │   │       │   │   └── slice_sync
│   │   │   │   │   │   │   │   │   │       │   ├── iostats
│   │   │   │   │   │   │   │   │   │       │   ├── logical_block_size
│   │   │   │   │   │   │   │   │   │       │   ├── max_hw_sectors_kb
│   │   │   │   │   │   │   │   │   │       │   ├── max_integrity_segments
│   │   │   │   │   │   │   │   │   │       │   ├── max_sectors_kb
│   │   │   │   │   │   │   │   │   │       │   ├── max_segments
│   │   │   │   │   │   │   │   │   │       │   ├── max_segment_size
│   │   │   │   │   │   │   │   │   │       │   ├── minimum_io_size
│   │   │   │   │   │   │   │   │   │       │   ├── nomerges
│   │   │   │   │   │   │   │   │   │       │   ├── nr_requests
│   │   │   │   │   │   │   │   │   │       │   ├── optimal_io_size
│   │   │   │   │   │   │   │   │   │       │   ├── physical_block_size
│   │   │   │   │   │   │   │   │   │       │   ├── read_ahead_kb
│   │   │   │   │   │   │   │   │   │       │   ├── rotational
│   │   │   │   │   │   │   │   │   │       │   ├── rq_affinity
│   │   │   │   │   │   │   │   │   │       │   └── scheduler
│   │   │   │   │   │   │   │   │   │       ├── range
│   │   │   │   │   │   │   │   │   │       ├── removable
│   │   │   │   │   │   │   │   │   │       ├── ro
│   │   │   │   │   │   │   │   │   │       ├── size
│   │   │   │   │   │   │   │   │   │       ├── slaves
│   │   │   │   │   │   │   │   │   │       ├── stat
│   │   │   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../../../class/block
│   │   │   │   │   │   │   │   │   │       ├── trace
│   │   │   │   │   │   │   │   │   │       │   ├── act_mask
│   │   │   │   │   │   │   │   │   │       │   ├── enable
│   │   │   │   │   │   │   │   │   │       │   ├── end_lba
│   │   │   │   │   │   │   │   │   │       │   ├── pid
│   │   │   │   │   │   │   │   │   │       │   └── start_lba
│   │   │   │   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   │   │   │   ├── bsg
│   │   │   │   │   │   │   │   │   │   └── 6:0:0:0
│   │   │   │   │   │   │   │   │   │       ├── dev
│   │   │   │   │   │   │   │   │   │       ├── device -> ../../../6:0:0:0
│   │   │   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../../../class/bsg
│   │   │   │   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   │   │   │   ├── delete
│   │   │   │   │   │   │   │   │   ├── device_blocked
│   │   │   │   │   │   │   │   │   ├── dh_state
│   │   │   │   │   │   │   │   │   ├── driver -> ../../../../../../../../../../../bus/scsi/drivers/sd
│   │   │   │   │   │   │   │   │   ├── evt_media_change
│   │   │   │   │   │   │   │   │   ├── generic -> scsi_generic/sg4
│   │   │   │   │   │   │   │   │   ├── iocounterbits
│   │   │   │   │   │   │   │   │   ├── iodone_cnt
│   │   │   │   │   │   │   │   │   ├── ioerr_cnt
│   │   │   │   │   │   │   │   │   ├── iorequest_cnt
│   │   │   │   │   │   │   │   │   ├── max_sectors
│   │   │   │   │   │   │   │   │   ├── modalias
│   │   │   │   │   │   │   │   │   ├── model
│   │   │   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   │   │   ├── queue_depth
│   │   │   │   │   │   │   │   │   ├── queue_type
│   │   │   │   │   │   │   │   │   ├── rescan
│   │   │   │   │   │   │   │   │   ├── rev
│   │   │   │   │   │   │   │   │   ├── scsi_device
│   │   │   │   │   │   │   │   │   │   └── 6:0:0:0
│   │   │   │   │   │   │   │   │   │       ├── device -> ../../../6:0:0:0
│   │   │   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../../../class/scsi_device
│   │   │   │   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   │   │   │   ├── scsi_disk
│   │   │   │   │   │   │   │   │   │   └── 6:0:0:0
│   │   │   │   │   │   │   │   │   │       ├── allow_restart
│   │   │   │   │   │   │   │   │   │       ├── app_tag_own
│   │   │   │   │   │   │   │   │   │       ├── cache_type
│   │   │   │   │   │   │   │   │   │       ├── device -> ../../../6:0:0:0
│   │   │   │   │   │   │   │   │   │       ├── FUA
│   │   │   │   │   │   │   │   │   │       ├── manage_start_stop
│   │   │   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │   │   │       ├── protection_mode
│   │   │   │   │   │   │   │   │   │       ├── protection_type
│   │   │   │   │   │   │   │   │   │       ├── provisioning_mode
│   │   │   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../../../class/scsi_disk
│   │   │   │   │   │   │   │   │   │       ├── thin_provisioning
│   │   │   │   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   │   │   │   ├── scsi_generic
│   │   │   │   │   │   │   │   │   │   └── sg4
│   │   │   │   │   │   │   │   │   │       ├── dev
│   │   │   │   │   │   │   │   │   │       ├── device -> ../../../6:0:0:0
│   │   │   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../../../class/scsi_generic
│   │   │   │   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   │   │   │   ├── scsi_level
│   │   │   │   │   │   │   │   │   ├── state
│   │   │   │   │   │   │   │   │   ├── subsystem -> ../../../../../../../../../../../bus/scsi
│   │   │   │   │   │   │   │   │   ├── timeout
│   │   │   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   │   │   └── vendor
│   │   │   │   │   │   │   │   ├── 6:0:0:1
│   │   │   │   │   │   │   │   │   ├── block
│   │   │   │   │   │   │   │   │   │   └── sdd
│   │   │   │   │   │   │   │   │   │       ├── alignment_offset
│   │   │   │   │   │   │   │   │   │       ├── bdi -> ../../../../../../../../../../../../virtual/bdi/8:48
│   │   │   │   │   │   │   │   │   │       ├── capability
│   │   │   │   │   │   │   │   │   │       ├── dev
│   │   │   │   │   │   │   │   │   │       ├── device -> ../../../6:0:0:1
│   │   │   │   │   │   │   │   │   │       ├── discard_alignment
│   │   │   │   │   │   │   │   │   │       ├── events
│   │   │   │   │   │   │   │   │   │       ├── events_async
│   │   │   │   │   │   │   │   │   │       ├── events_poll_msecs
│   │   │   │   │   │   │   │   │   │       ├── ext_range
│   │   │   │   │   │   │   │   │   │       ├── holders
│   │   │   │   │   │   │   │   │   │       ├── inflight
│   │   │   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │   │   │       ├── queue
│   │   │   │   │   │   │   │   │   │       │   ├── add_random
│   │   │   │   │   │   │   │   │   │       │   ├── discard_granularity
│   │   │   │   │   │   │   │   │   │       │   ├── discard_max_bytes
│   │   │   │   │   │   │   │   │   │       │   ├── discard_zeroes_data
│   │   │   │   │   │   │   │   │   │       │   ├── hw_sector_size
│   │   │   │   │   │   │   │   │   │       │   ├── iosched
│   │   │   │   │   │   │   │   │   │       │   │   ├── back_seek_max
│   │   │   │   │   │   │   │   │   │       │   │   ├── back_seek_penalty
│   │   │   │   │   │   │   │   │   │       │   │   ├── fifo_expire_async
│   │   │   │   │   │   │   │   │   │       │   │   ├── fifo_expire_sync
│   │   │   │   │   │   │   │   │   │       │   │   ├── group_idle
│   │   │   │   │   │   │   │   │   │       │   │   ├── low_latency
│   │   │   │   │   │   │   │   │   │       │   │   ├── quantum
│   │   │   │   │   │   │   │   │   │       │   │   ├── slice_async
│   │   │   │   │   │   │   │   │   │       │   │   ├── slice_async_rq
│   │   │   │   │   │   │   │   │   │       │   │   ├── slice_idle
│   │   │   │   │   │   │   │   │   │       │   │   └── slice_sync
│   │   │   │   │   │   │   │   │   │       │   ├── iostats
│   │   │   │   │   │   │   │   │   │       │   ├── logical_block_size
│   │   │   │   │   │   │   │   │   │       │   ├── max_hw_sectors_kb
│   │   │   │   │   │   │   │   │   │       │   ├── max_integrity_segments
│   │   │   │   │   │   │   │   │   │       │   ├── max_sectors_kb
│   │   │   │   │   │   │   │   │   │       │   ├── max_segments
│   │   │   │   │   │   │   │   │   │       │   ├── max_segment_size
│   │   │   │   │   │   │   │   │   │       │   ├── minimum_io_size
│   │   │   │   │   │   │   │   │   │       │   ├── nomerges
│   │   │   │   │   │   │   │   │   │       │   ├── nr_requests
│   │   │   │   │   │   │   │   │   │       │   ├── optimal_io_size
│   │   │   │   │   │   │   │   │   │       │   ├── physical_block_size
│   │   │   │   │   │   │   │   │   │       │   ├── read_ahead_kb
│   │   │   │   │   │   │   │   │   │       │   ├── rotational
│   │   │   │   │   │   │   │   │   │       │   ├── rq_affinity
│   │   │   │   │   │   │   │   │   │       │   └── scheduler
│   │   │   │   │   │   │   │   │   │       ├── range
│   │   │   │   │   │   │   │   │   │       ├── removable
│   │   │   │   │   │   │   │   │   │       ├── ro
│   │   │   │   │   │   │   │   │   │       ├── size
│   │   │   │   │   │   │   │   │   │       ├── slaves
│   │   │   │   │   │   │   │   │   │       ├── stat
│   │   │   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../../../class/block
│   │   │   │   │   │   │   │   │   │       ├── trace
│   │   │   │   │   │   │   │   │   │       │   ├── act_mask
│   │   │   │   │   │   │   │   │   │       │   ├── enable
│   │   │   │   │   │   │   │   │   │       │   ├── end_lba
│   │   │   │   │   │   │   │   │   │       │   ├── pid
│   │   │   │   │   │   │   │   │   │       │   └── start_lba
│   │   │   │   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   │   │   │   ├── bsg
│   │   │   │   │   │   │   │   │   │   └── 6:0:0:1
│   │   │   │   │   │   │   │   │   │       ├── dev
│   │   │   │   │   │   │   │   │   │       ├── device -> ../../../6:0:0:1
│   │   │   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../../../class/bsg
│   │   │   │   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   │   │   │   ├── delete
│   │   │   │   │   │   │   │   │   ├── device_blocked
│   │   │   │   │   │   │   │   │   ├── dh_state
│   │   │   │   │   │   │   │   │   ├── driver -> ../../../../../../../../../../../bus/scsi/drivers/sd
│   │   │   │   │   │   │   │   │   ├── evt_media_change
│   │   │   │   │   │   │   │   │   ├── generic -> scsi_generic/sg5
│   │   │   │   │   │   │   │   │   ├── iocounterbits
│   │   │   │   │   │   │   │   │   ├── iodone_cnt
│   │   │   │   │   │   │   │   │   ├── ioerr_cnt
│   │   │   │   │   │   │   │   │   ├── iorequest_cnt
│   │   │   │   │   │   │   │   │   ├── max_sectors
│   │   │   │   │   │   │   │   │   ├── modalias
│   │   │   │   │   │   │   │   │   ├── model
│   │   │   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   │   │   ├── queue_depth
│   │   │   │   │   │   │   │   │   ├── queue_type
│   │   │   │   │   │   │   │   │   ├── rescan
│   │   │   │   │   │   │   │   │   ├── rev
│   │   │   │   │   │   │   │   │   ├── scsi_device
│   │   │   │   │   │   │   │   │   │   └── 6:0:0:1
│   │   │   │   │   │   │   │   │   │       ├── device -> ../../../6:0:0:1
│   │   │   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../../../class/scsi_device
│   │   │   │   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   │   │   │   ├── scsi_disk
│   │   │   │   │   │   │   │   │   │   └── 6:0:0:1
│   │   │   │   │   │   │   │   │   │       ├── allow_restart
│   │   │   │   │   │   │   │   │   │       ├── app_tag_own
│   │   │   │   │   │   │   │   │   │       ├── cache_type
│   │   │   │   │   │   │   │   │   │       ├── device -> ../../../6:0:0:1
│   │   │   │   │   │   │   │   │   │       ├── FUA
│   │   │   │   │   │   │   │   │   │       ├── manage_start_stop
│   │   │   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │   │   │       ├── protection_mode
│   │   │   │   │   │   │   │   │   │       ├── protection_type
│   │   │   │   │   │   │   │   │   │       ├── provisioning_mode
│   │   │   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../../../class/scsi_disk
│   │   │   │   │   │   │   │   │   │       ├── thin_provisioning
│   │   │   │   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   │   │   │   ├── scsi_generic
│   │   │   │   │   │   │   │   │   │   └── sg5
│   │   │   │   │   │   │   │   │   │       ├── dev
│   │   │   │   │   │   │   │   │   │       ├── device -> ../../../6:0:0:1
│   │   │   │   │   │   │   │   │   │       ├── power
│   │   │   │   │   │   │   │   │   │       │   ├── async
│   │   │   │   │   │   │   │   │   │       │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   │       │   ├── control
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_status
│   │   │   │   │   │   │   │   │   │       │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   │       │   └── runtime_usage
│   │   │   │   │   │   │   │   │   │       ├── subsystem -> ../../../../../../../../../../../../../class/scsi_generic
│   │   │   │   │   │   │   │   │   │       └── uevent
│   │   │   │   │   │   │   │   │   ├── scsi_level
│   │   │   │   │   │   │   │   │   ├── state
│   │   │   │   │   │   │   │   │   ├── subsystem -> ../../../../../../../../../../../bus/scsi
│   │   │   │   │   │   │   │   │   ├── timeout
│   │   │   │   │   │   │   │   │   ├── type
│   │   │   │   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   │   │   │   └── vendor
│   │   │   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   │   │   ├── subsystem -> ../../../../../../../../../../bus/scsi
│   │   │   │   │   │   │   │   └── uevent
│   │   │   │   │   │   │   └── uevent
│   │   │   │   │   │   ├── interface
│   │   │   │   │   │   ├── modalias
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── subsystem -> ../../../../../../../../bus/usb
│   │   │   │   │   │   ├── supports_autosuspend
│   │   │   │   │   │   └── uevent
│   │   │   │   │   ├── authorized
│   │   │   │   │   ├── avoid_reset_quirk
│   │   │   │   │   ├── bcdDevice
│   │   │   │   │   ├── bConfigurationValue
│   │   │   │   │   ├── bDeviceClass
│   │   │   │   │   ├── bDeviceProtocol
│   │   │   │   │   ├── bDeviceSubClass
│   │   │   │   │   ├── bmAttributes
│   │   │   │   │   ├── bMaxPacketSize0
│   │   │   │   │   ├── bMaxPower
│   │   │   │   │   ├── bNumConfigurations
│   │   │   │   │   ├── bNumInterfaces
│   │   │   │   │   ├── busnum
│   │   │   │   │   ├── configuration
│   │   │   │   │   ├── descriptors
│   │   │   │   │   ├── dev
│   │   │   │   │   ├── devnum
│   │   │   │   │   ├── devpath
│   │   │   │   │   ├── driver -> ../../../../../../../bus/usb/drivers/usb
│   │   │   │   │   ├── ep_00
│   │   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   │   ├── bInterval
│   │   │   │   │   │   ├── bLength
│   │   │   │   │   │   ├── bmAttributes
│   │   │   │   │   │   ├── direction
│   │   │   │   │   │   ├── interval
│   │   │   │   │   │   ├── power
│   │   │   │   │   │   │   ├── async
│   │   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   │   ├── control
│   │   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   │   ├── type
│   │   │   │   │   │   ├── uevent
│   │   │   │   │   │   └── wMaxPacketSize
│   │   │   │   │   ├── idProduct
│   │   │   │   │   ├── idVendor
│   │   │   │   │   ├── manufacturer
│   │   │   │   │   ├── maxchild
│   │   │   │   │   ├── power
│   │   │   │   │   │   ├── active_duration
│   │   │   │   │   │   ├── async
│   │   │   │   │   │   ├── autosuspend
│   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   ├── connected_duration
│   │   │   │   │   │   ├── control
│   │   │   │   │   │   ├── level
│   │   │   │   │   │   ├── persist
│   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   ├── product
│   │   │   │   │   ├── quirks
│   │   │   │   │   ├── remove
│   │   │   │   │   ├── serial
│   │   │   │   │   ├── speed
│   │   │   │   │   ├── subsystem -> ../../../../../../../bus/usb
│   │   │   │   │   ├── uevent
│   │   │   │   │   ├── urbnum
│   │   │   │   │   └── version
│   │   │   │   ├── authorized
│   │   │   │   ├── avoid_reset_quirk
│   │   │   │   ├── bcdDevice
│   │   │   │   ├── bConfigurationValue
│   │   │   │   ├── bDeviceClass
│   │   │   │   ├── bDeviceProtocol
│   │   │   │   ├── bDeviceSubClass
│   │   │   │   ├── bmAttributes
│   │   │   │   ├── bMaxPacketSize0
│   │   │   │   ├── bMaxPower
│   │   │   │   ├── bNumConfigurations
│   │   │   │   ├── bNumInterfaces
│   │   │   │   ├── busnum
│   │   │   │   ├── configuration
│   │   │   │   ├── descriptors
│   │   │   │   ├── dev
│   │   │   │   ├── devnum
│   │   │   │   ├── devpath
│   │   │   │   ├── driver -> ../../../../../../bus/usb/drivers/usb
│   │   │   │   ├── ep_00
│   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   ├── bInterval
│   │   │   │   │   ├── bLength
│   │   │   │   │   ├── bmAttributes
│   │   │   │   │   ├── direction
│   │   │   │   │   ├── interval
│   │   │   │   │   ├── power
│   │   │   │   │   │   ├── async
│   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   ├── control
│   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   ├── type
│   │   │   │   │   ├── uevent
│   │   │   │   │   └── wMaxPacketSize
│   │   │   │   ├── idProduct
│   │   │   │   ├── idVendor
│   │   │   │   ├── maxchild
│   │   │   │   ├── power
│   │   │   │   │   ├── active_duration
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── connected_duration
│   │   │   │   │   ├── control
│   │   │   │   │   ├── level
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   ├── runtime_usage
│   │   │   │   │   ├── wakeup
│   │   │   │   │   ├── wakeup_active
│   │   │   │   │   ├── wakeup_active_count
│   │   │   │   │   ├── wakeup_count
│   │   │   │   │   ├── wakeup_hit_count
│   │   │   │   │   ├── wakeup_last_time_ms
│   │   │   │   │   ├── wakeup_max_time_ms
│   │   │   │   │   └── wakeup_total_time_ms
│   │   │   │   ├── product
│   │   │   │   ├── quirks
│   │   │   │   ├── remove
│   │   │   │   ├── speed
│   │   │   │   ├── subsystem -> ../../../../../../bus/usb
│   │   │   │   ├── uevent
│   │   │   │   ├── urbnum
│   │   │   │   └── version
│   │   │   ├── authorized
│   │   │   ├── authorized_default
│   │   │   ├── avoid_reset_quirk
│   │   │   ├── bcdDevice
│   │   │   ├── bConfigurationValue
│   │   │   ├── bDeviceClass
│   │   │   ├── bDeviceProtocol
│   │   │   ├── bDeviceSubClass
│   │   │   ├── bmAttributes
│   │   │   ├── bMaxPacketSize0
│   │   │   ├── bMaxPower
│   │   │   ├── bNumConfigurations
│   │   │   ├── bNumInterfaces
│   │   │   ├── busnum
│   │   │   ├── configuration
│   │   │   ├── descriptors
│   │   │   ├── dev
│   │   │   ├── devnum
│   │   │   ├── devpath
│   │   │   ├── driver -> ../../../../../bus/usb/drivers/usb
│   │   │   ├── ep_00
│   │   │   │   ├── bEndpointAddress
│   │   │   │   ├── bInterval
│   │   │   │   ├── bLength
│   │   │   │   ├── bmAttributes
│   │   │   │   ├── direction
│   │   │   │   ├── interval
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── control
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   ├── type
│   │   │   │   ├── uevent
│   │   │   │   └── wMaxPacketSize
│   │   │   ├── idProduct
│   │   │   ├── idVendor
│   │   │   ├── manufacturer
│   │   │   ├── maxchild
│   │   │   ├── power
│   │   │   │   ├── active_duration
│   │   │   │   ├── async
│   │   │   │   ├── autosuspend
│   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   ├── connected_duration
│   │   │   │   ├── control
│   │   │   │   ├── level
│   │   │   │   ├── runtime_active_kids
│   │   │   │   ├── runtime_active_time
│   │   │   │   ├── runtime_enabled
│   │   │   │   ├── runtime_status
│   │   │   │   ├── runtime_suspended_time
│   │   │   │   ├── runtime_usage
│   │   │   │   ├── wakeup
│   │   │   │   ├── wakeup_active
│   │   │   │   ├── wakeup_active_count
│   │   │   │   ├── wakeup_count
│   │   │   │   ├── wakeup_hit_count
│   │   │   │   ├── wakeup_last_time_ms
│   │   │   │   ├── wakeup_max_time_ms
│   │   │   │   └── wakeup_total_time_ms
│   │   │   ├── product
│   │   │   ├── quirks
│   │   │   ├── remove
│   │   │   ├── serial
│   │   │   ├── speed
│   │   │   ├── subsystem -> ../../../../../bus/usb
│   │   │   ├── uevent
│   │   │   ├── urbnum
│   │   │   └── version
│   │   ├── usbmon
│   │   │   └── usbmon2
│   │   │       ├── dev
│   │   │       ├── device -> ../../../0000:02:00.0
│   │   │       ├── power
│   │   │       │   ├── async
│   │   │       │   ├── autosuspend_delay_ms
│   │   │       │   ├── control
│   │   │       │   ├── runtime_active_kids
│   │   │       │   ├── runtime_active_time
│   │   │       │   ├── runtime_enabled
│   │   │       │   ├── runtime_status
│   │   │       │   ├── runtime_suspended_time
│   │   │       │   └── runtime_usage
│   │   │       ├── subsystem -> ../../../../../../class/usbmon
│   │   │       └── uevent
│   │   └── vendor
│   ├── 0000:02:01.0
│   │   ├── broken_parity_status
│   │   ├── class
│   │   ├── config
│   │   ├── consistent_dma_mask_bits
│   │   ├── device
│   │   ├── dma_mask_bits
│   │   ├── driver -> ../../../../bus/pci/drivers/e1000
│   │   ├── enable
│   │   ├── firmware_node -> ../../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:05/device:07
│   │   ├── irq
│   │   ├── local_cpulist
│   │   ├── local_cpus
│   │   ├── modalias
│   │   ├── msi_bus
│   │   ├── net
│   │   │   └── eth0
│   │   │       ├── addr_assign_type
│   │   │       ├── address
│   │   │       ├── addr_len
│   │   │       ├── broadcast
│   │   │       ├── carrier
│   │   │       ├── device -> ../../../0000:02:01.0
│   │   │       ├── dev_id
│   │   │       ├── dormant
│   │   │       ├── duplex
│   │   │       ├── flags
│   │   │       ├── ifalias
│   │   │       ├── ifindex
│   │   │       ├── iflink
│   │   │       ├── link_mode
│   │   │       ├── mtu
│   │   │       ├── netdev_group
│   │   │       ├── operstate
│   │   │       ├── power
│   │   │       │   ├── async
│   │   │       │   ├── autosuspend_delay_ms
│   │   │       │   ├── control
│   │   │       │   ├── runtime_active_kids
│   │   │       │   ├── runtime_active_time
│   │   │       │   ├── runtime_enabled
│   │   │       │   ├── runtime_status
│   │   │       │   ├── runtime_suspended_time
│   │   │       │   └── runtime_usage
│   │   │       ├── queues
│   │   │       │   ├── rx-0
│   │   │       │   │   ├── rps_cpus
│   │   │       │   │   └── rps_flow_cnt
│   │   │       │   └── tx-0
│   │   │       │       └── xps_cpus
│   │   │       ├── speed
│   │   │       ├── statistics
│   │   │       │   ├── collisions
│   │   │       │   ├── multicast
│   │   │       │   ├── rx_bytes
│   │   │       │   ├── rx_compressed
│   │   │       │   ├── rx_crc_errors
│   │   │       │   ├── rx_dropped
│   │   │       │   ├── rx_errors
│   │   │       │   ├── rx_fifo_errors
│   │   │       │   ├── rx_frame_errors
│   │   │       │   ├── rx_length_errors
│   │   │       │   ├── rx_missed_errors
│   │   │       │   ├── rx_over_errors
│   │   │       │   ├── rx_packets
│   │   │       │   ├── tx_aborted_errors
│   │   │       │   ├── tx_bytes
│   │   │       │   ├── tx_carrier_errors
│   │   │       │   ├── tx_compressed
│   │   │       │   ├── tx_dropped
│   │   │       │   ├── tx_errors
│   │   │       │   ├── tx_fifo_errors
│   │   │       │   ├── tx_heartbeat_errors
│   │   │       │   ├── tx_packets
│   │   │       │   └── tx_window_errors
│   │   │       ├── subsystem -> ../../../../../../class/net
│   │   │       ├── tx_queue_len
│   │   │       ├── type
│   │   │       └── uevent
│   │   ├── numa_node
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   ├── runtime_usage
│   │   │   ├── wakeup
│   │   │   ├── wakeup_active
│   │   │   ├── wakeup_active_count
│   │   │   ├── wakeup_count
│   │   │   ├── wakeup_hit_count
│   │   │   ├── wakeup_last_time_ms
│   │   │   ├── wakeup_max_time_ms
│   │   │   └── wakeup_total_time_ms
│   │   ├── remove
│   │   ├── rescan
│   │   ├── reset
│   │   ├── resource
│   │   ├── resource0
│   │   ├── resource2
│   │   ├── resource4
│   │   ├── rom
│   │   ├── subsystem -> ../../../../bus/pci
│   │   ├── subsystem_device
│   │   ├── subsystem_vendor
│   │   ├── uevent
│   │   └── vendor
│   ├── 0000:02:02.0
│   │   ├── 0-0:CS4297A
│   │   │   ├── power
│   │   │   │   ├── async
│   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   ├── control
│   │   │   │   ├── runtime_active_kids
│   │   │   │   ├── runtime_active_time
│   │   │   │   ├── runtime_enabled
│   │   │   │   ├── runtime_status
│   │   │   │   ├── runtime_suspended_time
│   │   │   │   └── runtime_usage
│   │   │   ├── subsystem -> ../../../../../bus/ac97
│   │   │   └── uevent
│   │   ├── broken_parity_status
│   │   ├── class
│   │   ├── config
│   │   ├── consistent_dma_mask_bits
│   │   ├── device
│   │   ├── dma_mask_bits
│   │   ├── driver -> ../../../../bus/pci/drivers/snd_ens1371
│   │   ├── enable
│   │   ├── firmware_node -> ../../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:05/device:08
│   │   ├── irq
│   │   ├── local_cpulist
│   │   ├── local_cpus
│   │   ├── modalias
│   │   ├── msi_bus
│   │   ├── numa_node
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   ├── runtime_usage
│   │   │   ├── wakeup
│   │   │   ├── wakeup_active
│   │   │   ├── wakeup_active_count
│   │   │   ├── wakeup_count
│   │   │   ├── wakeup_hit_count
│   │   │   ├── wakeup_last_time_ms
│   │   │   ├── wakeup_max_time_ms
│   │   │   └── wakeup_total_time_ms
│   │   ├── remove
│   │   ├── rescan
│   │   ├── resource
│   │   ├── resource0
│   │   ├── sound
│   │   │   └── card0
│   │   │       ├── controlC0
│   │   │       │   ├── dev
│   │   │       │   ├── device -> ../../card0
│   │   │       │   ├── power
│   │   │       │   │   ├── async
│   │   │       │   │   ├── autosuspend_delay_ms
│   │   │       │   │   ├── control
│   │   │       │   │   ├── runtime_active_kids
│   │   │       │   │   ├── runtime_active_time
│   │   │       │   │   ├── runtime_enabled
│   │   │       │   │   ├── runtime_status
│   │   │       │   │   ├── runtime_suspended_time
│   │   │       │   │   └── runtime_usage
│   │   │       │   ├── subsystem -> ../../../../../../../class/sound
│   │   │       │   └── uevent
│   │   │       ├── device -> ../../../0000:02:02.0
│   │   │       ├── dmmidi
│   │   │       │   ├── dev
│   │   │       │   ├── device -> ../../card0
│   │   │       │   ├── power
│   │   │       │   │   ├── async
│   │   │       │   │   ├── autosuspend_delay_ms
│   │   │       │   │   ├── control
│   │   │       │   │   ├── runtime_active_kids
│   │   │       │   │   ├── runtime_active_time
│   │   │       │   │   ├── runtime_enabled
│   │   │       │   │   ├── runtime_status
│   │   │       │   │   ├── runtime_suspended_time
│   │   │       │   │   └── runtime_usage
│   │   │       │   ├── subsystem -> ../../../../../../../class/sound
│   │   │       │   └── uevent
│   │   │       ├── id
│   │   │       ├── midi
│   │   │       │   ├── dev
│   │   │       │   ├── device -> ../../card0
│   │   │       │   ├── power
│   │   │       │   │   ├── async
│   │   │       │   │   ├── autosuspend_delay_ms
│   │   │       │   │   ├── control
│   │   │       │   │   ├── runtime_active_kids
│   │   │       │   │   ├── runtime_active_time
│   │   │       │   │   ├── runtime_enabled
│   │   │       │   │   ├── runtime_status
│   │   │       │   │   ├── runtime_suspended_time
│   │   │       │   │   └── runtime_usage
│   │   │       │   ├── subsystem -> ../../../../../../../class/sound
│   │   │       │   └── uevent
│   │   │       ├── midiC0D0
│   │   │       │   ├── dev
│   │   │       │   ├── device -> ../../card0
│   │   │       │   ├── power
│   │   │       │   │   ├── async
│   │   │       │   │   ├── autosuspend_delay_ms
│   │   │       │   │   ├── control
│   │   │       │   │   ├── runtime_active_kids
│   │   │       │   │   ├── runtime_active_time
│   │   │       │   │   ├── runtime_enabled
│   │   │       │   │   ├── runtime_status
│   │   │       │   │   ├── runtime_suspended_time
│   │   │       │   │   └── runtime_usage
│   │   │       │   ├── subsystem -> ../../../../../../../class/sound
│   │   │       │   └── uevent
│   │   │       ├── number
│   │   │       ├── pcmC0D0c
│   │   │       │   ├── dev
│   │   │       │   ├── device -> ../../card0
│   │   │       │   ├── pcm_class
│   │   │       │   ├── power
│   │   │       │   │   ├── async
│   │   │       │   │   ├── autosuspend_delay_ms
│   │   │       │   │   ├── control
│   │   │       │   │   ├── runtime_active_kids
│   │   │       │   │   ├── runtime_active_time
│   │   │       │   │   ├── runtime_enabled
│   │   │       │   │   ├── runtime_status
│   │   │       │   │   ├── runtime_suspended_time
│   │   │       │   │   └── runtime_usage
│   │   │       │   ├── subsystem -> ../../../../../../../class/sound
│   │   │       │   └── uevent
│   │   │       ├── pcmC0D0p
│   │   │       │   ├── dev
│   │   │       │   ├── device -> ../../card0
│   │   │       │   ├── pcm_class
│   │   │       │   ├── power
│   │   │       │   │   ├── async
│   │   │       │   │   ├── autosuspend_delay_ms
│   │   │       │   │   ├── control
│   │   │       │   │   ├── runtime_active_kids
│   │   │       │   │   ├── runtime_active_time
│   │   │       │   │   ├── runtime_enabled
│   │   │       │   │   ├── runtime_status
│   │   │       │   │   ├── runtime_suspended_time
│   │   │       │   │   └── runtime_usage
│   │   │       │   ├── subsystem -> ../../../../../../../class/sound
│   │   │       │   └── uevent
│   │   │       ├── pcmC0D1p
│   │   │       │   ├── dev
│   │   │       │   ├── device -> ../../card0
│   │   │       │   ├── pcm_class
│   │   │       │   ├── power
│   │   │       │   │   ├── async
│   │   │       │   │   ├── autosuspend_delay_ms
│   │   │       │   │   ├── control
│   │   │       │   │   ├── runtime_active_kids
│   │   │       │   │   ├── runtime_active_time
│   │   │       │   │   ├── runtime_enabled
│   │   │       │   │   ├── runtime_status
│   │   │       │   │   ├── runtime_suspended_time
│   │   │       │   │   └── runtime_usage
│   │   │       │   ├── subsystem -> ../../../../../../../class/sound
│   │   │       │   └── uevent
│   │   │       ├── power
│   │   │       │   ├── async
│   │   │       │   ├── autosuspend_delay_ms
│   │   │       │   ├── control
│   │   │       │   ├── runtime_active_kids
│   │   │       │   ├── runtime_active_time
│   │   │       │   ├── runtime_enabled
│   │   │       │   ├── runtime_status
│   │   │       │   ├── runtime_suspended_time
│   │   │       │   └── runtime_usage
│   │   │       ├── subsystem -> ../../../../../../class/sound
│   │   │       └── uevent
│   │   ├── subsystem -> ../../../../bus/pci
│   │   ├── subsystem_device
│   │   ├── subsystem_vendor
│   │   ├── uevent
│   │   └── vendor
│   ├── 0000:02:03.0
│   │   ├── broken_parity_status
│   │   ├── class
│   │   ├── companion
│   │   ├── config
│   │   ├── consistent_dma_mask_bits
│   │   ├── device
│   │   ├── dma_mask_bits
│   │   ├── driver -> ../../../../bus/pci/drivers/ehci_hcd
│   │   ├── enable
│   │   ├── firmware_node -> ../../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:05/device:09
│   │   ├── irq
│   │   ├── local_cpulist
│   │   ├── local_cpus
│   │   ├── modalias
│   │   ├── msi_bus
│   │   ├── numa_node
│   │   ├── pools
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   ├── runtime_usage
│   │   │   ├── wakeup
│   │   │   ├── wakeup_active
│   │   │   ├── wakeup_active_count
│   │   │   ├── wakeup_count
│   │   │   ├── wakeup_hit_count
│   │   │   ├── wakeup_last_time_ms
│   │   │   ├── wakeup_max_time_ms
│   │   │   └── wakeup_total_time_ms
│   │   ├── remove
│   │   ├── rescan
│   │   ├── resource
│   │   ├── resource0
│   │   ├── subsystem -> ../../../../bus/pci
│   │   ├── subsystem_device
│   │   ├── subsystem_vendor
│   │   ├── uevent
│   │   ├── uframe_periodic_max
│   │   ├── usb1
│   │   │   ├── 1-0:1.0
│   │   │   │   ├── bAlternateSetting
│   │   │   │   ├── bInterfaceClass
│   │   │   │   ├── bInterfaceNumber
│   │   │   │   ├── bInterfaceProtocol
│   │   │   │   ├── bInterfaceSubClass
│   │   │   │   ├── bNumEndpoints
│   │   │   │   ├── driver -> ../../../../../../bus/usb/drivers/hub
│   │   │   │   ├── ep_81
│   │   │   │   │   ├── bEndpointAddress
│   │   │   │   │   ├── bInterval
│   │   │   │   │   ├── bLength
│   │   │   │   │   ├── bmAttributes
│   │   │   │   │   ├── direction
│   │   │   │   │   ├── interval
│   │   │   │   │   ├── power
│   │   │   │   │   │   ├── async
│   │   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   │   ├── control
│   │   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   │   ├── runtime_status
│   │   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   │   └── runtime_usage
│   │   │   │   │   ├── type
│   │   │   │   │   ├── uevent
│   │   │   │   │   └── wMaxPacketSize
│   │   │   │   ├── modalias
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   └── runtime_usage
│   │   │   │   ├── subsystem -> ../../../../../../bus/usb
│   │   │   │   ├── supports_autosuspend
│   │   │   │   └── uevent
│   │   │   ├── authorized
│   │   │   ├── authorized_default
│   │   │   ├── avoid_reset_quirk
│   │   │   ├── bcdDevice
│   │   │   ├── bConfigurationValue
│   │   │   ├── bDeviceClass
│   │   │   ├── bDeviceProtocol
│   │   │   ├── bDeviceSubClass
│   │   │   ├── bmAttributes
│   │   │   ├── bMaxPacketSize0
│   │   │   ├── bMaxPower
│   │   │   ├── bNumConfigurations
│   │   │   ├── bNumInterfaces
│   │   │   ├── busnum
│   │   │   ├── configuration
│   │   │   ├── descriptors
│   │   │   ├── dev
│   │   │   ├── devnum
│   │   │   ├── devpath
│   │   │   ├── driver -> ../../../../../bus/usb/drivers/usb
│   │   │   ├── ep_00
│   │   │   │   ├── bEndpointAddress
│   │   │   │   ├── bInterval
│   │   │   │   ├── bLength
│   │   │   │   ├── bmAttributes
│   │   │   │   ├── direction
│   │   │   │   ├── interval
│   │   │   │   ├── power
│   │   │   │   │   ├── async
│   │   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   │   ├── control
│   │   │   │   │   ├── runtime_active_kids
│   │   │   │   │   ├── runtime_active_time
│   │   │   │   │   ├── runtime_enabled
│   │   │   │   │   ├── runtime_status
│   │   │   │   │   ├── runtime_suspended_time
│   │   │   │   │   └── runtime_usage
│   │   │   │   ├── type
│   │   │   │   ├── uevent
│   │   │   │   └── wMaxPacketSize
│   │   │   ├── idProduct
│   │   │   ├── idVendor
│   │   │   ├── manufacturer
│   │   │   ├── maxchild
│   │   │   ├── power
│   │   │   │   ├── active_duration
│   │   │   │   ├── async
│   │   │   │   ├── autosuspend
│   │   │   │   ├── autosuspend_delay_ms
│   │   │   │   ├── connected_duration
│   │   │   │   ├── control
│   │   │   │   ├── level
│   │   │   │   ├── runtime_active_kids
│   │   │   │   ├── runtime_active_time
│   │   │   │   ├── runtime_enabled
│   │   │   │   ├── runtime_status
│   │   │   │   ├── runtime_suspended_time
│   │   │   │   ├── runtime_usage
│   │   │   │   ├── wakeup
│   │   │   │   ├── wakeup_active
│   │   │   │   ├── wakeup_active_count
│   │   │   │   ├── wakeup_count
│   │   │   │   ├── wakeup_hit_count
│   │   │   │   ├── wakeup_last_time_ms
│   │   │   │   ├── wakeup_max_time_ms
│   │   │   │   └── wakeup_total_time_ms
│   │   │   ├── product
│   │   │   ├── quirks
│   │   │   ├── remove
│   │   │   ├── serial
│   │   │   ├── speed
│   │   │   ├── subsystem -> ../../../../../bus/usb
│   │   │   ├── uevent
│   │   │   ├── urbnum
│   │   │   └── version
│   │   ├── usbmon
│   │   │   └── usbmon1
│   │   │       ├── dev
│   │   │       ├── device -> ../../../0000:02:03.0
│   │   │       ├── power
│   │   │       │   ├── async
│   │   │       │   ├── autosuspend_delay_ms
│   │   │       │   ├── control
│   │   │       │   ├── runtime_active_kids
│   │   │       │   ├── runtime_active_time
│   │   │       │   ├── runtime_enabled
│   │   │       │   ├── runtime_status
│   │   │       │   ├── runtime_suspended_time
│   │   │       │   └── runtime_usage
│   │   │       ├── subsystem -> ../../../../../../class/usbmon
│   │   │       └── uevent
│   │   └── vendor
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:05
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:02
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:11.0
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:15.0
│   ├── 0000:00:15.0:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:15.0:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:0a
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:03
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:15.0
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:15.1
│   ├── 0000:00:15.1:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:15.1:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:0e
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:04
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:15.1
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:15.2
│   ├── 0000:00:15.2:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:15.2:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:0f
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:05
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:15.2
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:15.3
│   ├── 0000:00:15.3:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:15.3:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:10
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:06
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:15.3
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:15.4
│   ├── 0000:00:15.4:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:15.4:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:11
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:07
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:15.4
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:15.5
│   ├── 0000:00:15.5:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:15.5:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:12
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:08
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:15.5
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:15.6
│   ├── 0000:00:15.6:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:15.6:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:13
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:09
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:15.6
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:15.7
│   ├── 0000:00:15.7:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:15.7:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:14
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:0a
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:15.7
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:16.0
│   ├── 0000:00:16.0:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:16.0:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:0b
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:0b
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:16.0
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:16.1
│   ├── 0000:00:16.1:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:16.1:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:15
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:0c
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:16.1
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:16.2
│   ├── 0000:00:16.2:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:16.2:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:16
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:0d
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:16.2
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:16.3
│   ├── 0000:00:16.3:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:16.3:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:17
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:0e
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:16.3
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:16.4
│   ├── 0000:00:16.4:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:16.4:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:18
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:0f
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:16.4
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:16.5
│   ├── 0000:00:16.5:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:16.5:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:19
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:10
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:16.5
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:16.6
│   ├── 0000:00:16.6:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:16.6:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:1a
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:11
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:16.6
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:16.7
│   ├── 0000:00:16.7:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:16.7:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:1b
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:12
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:16.7
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:17.0
│   ├── 0000:00:17.0:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:17.0:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:0c
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:13
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:17.0
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:17.1
│   ├── 0000:00:17.1:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:17.1:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:1c
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:14
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:17.1
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:17.2
│   ├── 0000:00:17.2:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:17.2:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:1d
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:15
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:17.2
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:17.3
│   ├── 0000:00:17.3:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:17.3:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:1e
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:16
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:17.3
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:17.4
│   ├── 0000:00:17.4:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:17.4:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:1f
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:17
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:17.4
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:17.5
│   ├── 0000:00:17.5:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:17.5:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:20
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:18
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:17.5
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:17.6
│   ├── 0000:00:17.6:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:17.6:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:21
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:19
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:17.6
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:17.7
│   ├── 0000:00:17.7:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:17.7:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:22
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:1a
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:17.7
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:18.0
│   ├── 0000:00:18.0:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:18.0:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:0d
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:1b
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:18.0
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:18.1
│   ├── 0000:00:18.1:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:18.1:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:23
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:1c
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:18.1
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:18.2
│   ├── 0000:00:18.2:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:18.2:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:24
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:1d
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:18.2
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:18.3
│   ├── 0000:00:18.3:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:18.3:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:25
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:1e
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:18.3
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:18.4
│   ├── 0000:00:18.4:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:18.4:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:26
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:1f
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:18.4
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:18.5
│   ├── 0000:00:18.5:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:18.5:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:27
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:20
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:18.5
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:18.6
│   ├── 0000:00:18.6:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:18.6:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:28
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:21
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:18.6
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── 0000:00:18.7
│   ├── 0000:00:18.7:pcie01
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pcie_pme
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── 0000:00:18.7:pcie04
│   │   ├── driver -> ../../../../bus/pci_express/drivers/pciehp
│   │   ├── power
│   │   │   ├── async
│   │   │   ├── autosuspend_delay_ms
│   │   │   ├── control
│   │   │   ├── runtime_active_kids
│   │   │   ├── runtime_active_time
│   │   │   ├── runtime_enabled
│   │   │   ├── runtime_status
│   │   │   ├── runtime_suspended_time
│   │   │   └── runtime_usage
│   │   ├── subsystem -> ../../../../bus/pci_express
│   │   └── uevent
│   ├── broken_parity_status
│   ├── class
│   ├── config
│   ├── consistent_dma_mask_bits
│   ├── device
│   ├── dma_mask_bits
│   ├── driver -> ../../../bus/pci/drivers/pcieport
│   ├── enable
│   ├── firmware_node -> ../../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/device:29
│   ├── irq
│   ├── local_cpulist
│   ├── local_cpus
│   ├── modalias
│   ├── msi_bus
│   ├── numa_node
│   ├── pci_bus
│   │   └── 0000:22
│   │       ├── cpuaffinity
│   │       ├── cpulistaffinity
│   │       ├── device -> ../../../0000:00:18.7
│   │       ├── power
│   │       │   ├── async
│   │       │   ├── autosuspend_delay_ms
│   │       │   ├── control
│   │       │   ├── runtime_active_kids
│   │       │   ├── runtime_active_time
│   │       │   ├── runtime_enabled
│   │       │   ├── runtime_status
│   │       │   ├── runtime_suspended_time
│   │       │   └── runtime_usage
│   │       ├── rescan
│   │       ├── subsystem -> ../../../../../class/pci_bus
│   │       └── uevent
│   ├── power
│   │   ├── async
│   │   ├── autosuspend_delay_ms
│   │   ├── control
│   │   ├── runtime_active_kids
│   │   ├── runtime_active_time
│   │   ├── runtime_enabled
│   │   ├── runtime_status
│   │   ├── runtime_suspended_time
│   │   ├── runtime_usage
│   │   ├── wakeup
│   │   ├── wakeup_active
│   │   ├── wakeup_active_count
│   │   ├── wakeup_count
│   │   ├── wakeup_hit_count
│   │   ├── wakeup_last_time_ms
│   │   ├── wakeup_max_time_ms
│   │   └── wakeup_total_time_ms
│   ├── remove
│   ├── rescan
│   ├── reset
│   ├── resource
│   ├── subsystem -> ../../../bus/pci
│   ├── subsystem_device
│   ├── subsystem_vendor
│   ├── uevent
│   └── vendor
├── firmware_node -> ../LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00
├── pci_bus
│   └── 0000:00
│       ├── cpuaffinity
│       ├── cpulistaffinity
│       ├── device -> ../../../pci0000:00
│       ├── power
│       │   ├── async
│       │   ├── autosuspend_delay_ms
│       │   ├── control
│       │   ├── runtime_active_kids
│       │   ├── runtime_active_time
│       │   ├── runtime_enabled
│       │   ├── runtime_status
│       │   ├── runtime_suspended_time
│       │   └── runtime_usage
│       ├── rescan
│       ├── subsystem -> ../../../../class/pci_bus
│       └── uevent
├── power
│   ├── async
│   ├── autosuspend_delay_ms
│   ├── control
│   ├── runtime_active_kids
│   ├── runtime_active_time
│   ├── runtime_enabled
│   ├── runtime_status
│   ├── runtime_suspended_time
│   ├── runtime_usage
│   ├── wakeup
│   ├── wakeup_active
│   ├── wakeup_active_count
│   ├── wakeup_count
│   ├── wakeup_hit_count
│   ├── wakeup_last_time_ms
│   ├── wakeup_max_time_ms
│   └── wakeup_total_time_ms
└── uevent

1225 directories, 5331 files
```
