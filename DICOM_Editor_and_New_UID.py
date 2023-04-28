import pydicom
import os
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout
from tkinter import Tk, filedialog
import sys
import glob


#make a folder/file option. - place another box at the end that allows you to apply the proposed changes to a whole folder
class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'RTPlan/Structure/CT/DRR DCM Modifier'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.initUI()


    def initUI(self):
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox_1)
        windowLayout.addWidget(self.horizontalGroupBox_2)
        windowLayout.addWidget(self.horizontalGroupBox_3)
        self.setLayout(windowLayout)
        self.show()

    def createGridLayout(self):
        # Widgets for horizontalGroupBox_1
        self.btn_fileopen = QPushButton('Open File', self)
        self.btn_fileopen.clicked.connect(self.fileopen)

        self.lbl_fileopen = QLabel('DCM File', self)
        self.edit_fileopen = QLabel('', self)

        # Widgets for horizontalGroupBox_2
        self.lbl_parameter = QLabel('PARAMETER', self)
        self.lbl_current_value = QLabel('CURRENT VALUE', self)
        self.lbl_edit_value = QLabel('PROPOSED CHANGE', self)

        self.lbl_Modality = QLabel('Modality', self)
        self.lbl_Modality_current = QLabel('', self)

        self.lbl_RTPlanName = QLabel('RTPlanName', self)
        self.lbl_RTPlanName_current = QLabel('', self)
        self.edit_RTPlanName = QLineEdit('', self)

        self.lbl_RTPlanLabel = QLabel('RTPlanLabel', self)
        self.lbl_RTPlanLabel_current = QLabel('', self)
        self.edit_RTPlanLabel = QLineEdit('', self)

        self.lbl_TreatmentMachineName = QLabel('TreatmentMachineName', self)
        self.lbl_TreatmentMachineName_current = QLabel('', self)
        self.edit_TreatmentMachineName = QLineEdit('', self)

        self.lbl_StudyDescription = QLabel('StudyDescription', self)
        self.lbl_StudyDescription_current = QLabel('', self)
        self.edit_StudyDescription = QLineEdit('', self)

        self.lbl_SeriesDescription = QLabel('SeriesDescription', self)
        self.lbl_SeriesDescription_current = QLabel('', self)
        self.edit_SeriesDescription = QLineEdit('', self)

        self.lbl_PatientName = QLabel('PatientName: LastName^FirstName', self)
        self.lbl_PatientName_current = QLabel('', self)
        self.edit_PatientName = QLineEdit('', self)

        self.lbl_PatientID = QLabel('PatientID', self)
        self.lbl_PatientID_current = QLabel('', self)
        self.edit_PatientID = QLineEdit('', self)

        self.lbl_PatientSex = QLabel('PatientSex', self)
        self.lbl_PatientSex_current = QLabel('', self)
        self.edit_PatientSex = QLineEdit('', self)

        self.lbl_PatientBirthDate = QLabel('PatientBirthDate', self)
        self.lbl_PatientBirthDate_current = QLabel('', self)
        self.edit_PatientBirthDate = QLineEdit('', self)

        self.btn_update_dcm = QPushButton('Update', self)
        self.btn_update_dcm.clicked.connect(self.update_dcm_and_update_gui)

        self.btn_filesave = QPushButton('Export', self)
        self.btn_filesave.clicked.connect(self.filesave)

        # Widgets for horizontalGroupBox_3
        self.lbl_input_folder = QLabel('Input Folder', self)
        self.lbl_input_folder_path = QLabel('',self)
        self.btn_folderopen = QPushButton('Open Folder', self)
        self.btn_folderopen.clicked.connect(self.folderopen)

        self.lbl_output_folder = QLabel('Output Folder', self)
        self.lbl_outputs_folder_path = QLabel('',self)
        self.btn_folderopen_output = QPushButton('Open Folder', self)
        self.btn_folderopen_output.clicked.connect(self.folderopen_output)

        self.lbl_progress_folder = QLabel('', self)
        self.lbl_status_folder = QLabel('', self)
        self.btn_activate_folder = QPushButton('Modify Entire Folder', self)
        self.btn_activate_folder.clicked.connect(self.activate_folder)
        self.btn_activate_folder_new_uid = QPushButton('Modify Entire Folder - With New UIDs', self)
        self.btn_activate_folder_new_uid.clicked.connect(self.activate_folder_new_UID)


        self.horizontalGroupBox_1 = QGroupBox("Open One DCM File")
        layout = QGridLayout()
        layout.setColumnStretch(1, 3)
        layout.addWidget(self.lbl_fileopen, 1, 1)
        layout.addWidget(self.edit_fileopen, 1, 2)
        layout.addWidget(self.btn_fileopen, 1, 3)
        self.horizontalGroupBox_1.setLayout(layout)

        self.horizontalGroupBox_2 = QGroupBox(
            "Modify DCM/Enter Proposed Changes")
        layout_2 = QGridLayout()
        layout_2.setColumnStretch(13, 3)
        layout_2.addWidget(self.lbl_parameter, 1, 1)
        layout_2.addWidget(self.lbl_current_value, 1, 2)
        layout_2.addWidget(self.lbl_edit_value, 1, 3)
        layout_2.addWidget(self.lbl_Modality, 2, 1)
        layout_2.addWidget(self.lbl_Modality_current, 2, 2)
        layout_2.addWidget(self.lbl_RTPlanName, 3, 1)
        layout_2.addWidget(self.lbl_RTPlanName_current, 3, 2)
        layout_2.addWidget(self.edit_RTPlanName, 3, 3)
        layout_2.addWidget(self.lbl_RTPlanLabel, 4, 1)
        layout_2.addWidget(self.lbl_RTPlanLabel_current, 4, 2)
        layout_2.addWidget(self.edit_RTPlanLabel, 4, 3)
        layout_2.addWidget(self.lbl_TreatmentMachineName, 5, 1)
        layout_2.addWidget(self.lbl_TreatmentMachineName_current, 5, 2)
        layout_2.addWidget(self.edit_TreatmentMachineName, 5, 3)
        layout_2.addWidget(self.lbl_StudyDescription, 6, 1)
        layout_2.addWidget(self.lbl_StudyDescription_current, 6, 2)
        layout_2.addWidget(self.edit_StudyDescription, 6, 3)
        layout_2.addWidget(self.lbl_SeriesDescription, 7, 1)
        layout_2.addWidget(self.lbl_SeriesDescription_current, 7, 2)
        layout_2.addWidget(self.edit_SeriesDescription, 7, 3)
        layout_2.addWidget(self.lbl_PatientName, 8, 1)
        layout_2.addWidget(self.lbl_PatientName_current, 8, 2)
        layout_2.addWidget(self.edit_PatientName, 8, 3)
        layout_2.addWidget(self.lbl_PatientID, 9, 1)
        layout_2.addWidget(self.lbl_PatientID_current, 9, 2)
        layout_2.addWidget(self.edit_PatientID, 9, 3)
        layout_2.addWidget(self.lbl_PatientSex, 10, 1)
        layout_2.addWidget(self.lbl_PatientSex_current, 10, 2)
        layout_2.addWidget(self.edit_PatientSex, 10, 3)
        layout_2.addWidget(self.lbl_PatientBirthDate, 11, 1)
        layout_2.addWidget(self.lbl_PatientBirthDate_current, 11, 2)
        layout_2.addWidget(self.edit_PatientBirthDate, 11, 3)
        layout_2.addWidget(self.btn_update_dcm, 12, 3)
        layout_2.addWidget(self.btn_filesave, 13, 3)
        self.horizontalGroupBox_2.setLayout(layout_2)

        self.horizontalGroupBox_3 = QGroupBox("Modify all DCM in folder with Proposed Changes")
        layout_3 = QGridLayout()
        layout_3.setColumnStretch(4, 3)
        layout_3.addWidget(self.lbl_input_folder, 1, 1)
        layout_3.addWidget(self.lbl_input_folder_path, 1, 2)
        layout_3.addWidget(self.btn_folderopen, 1, 3)
        layout_3.addWidget(self.lbl_output_folder, 2, 1)
        layout_3.addWidget(self.lbl_outputs_folder_path, 2, 2)
        layout_3.addWidget(self.btn_folderopen_output, 2, 3)
        layout_3.addWidget(self.lbl_progress_folder,3, 1)
        layout_3.addWidget(self.lbl_status_folder, 3, 2)
        layout_3.addWidget(self.btn_activate_folder, 3, 3)
        layout_3.addWidget(self.btn_activate_folder_new_uid, 4, 3)
        self.horizontalGroupBox_3.setLayout(layout_3)

    def reload_parameters_in_GUI(self,dcm):
        try:
            self.lbl_Modality_current.setText(dcm.Modality)
        except:
            self.lbl_Modality_current.setText('')

        try:
            self.lbl_RTPlanName_current.setText(dcm.RTPlanName)
        except:
            self.lbl_RTPlanName_current.setText('')

        try:
            self.lbl_RTPlanLabel_current.setText(dcm.RTPlanLabel)
        except:
            self.lbl_RTPlanLabel_current.setText('')
            
        try:
            self.lbl_TreatmentMachineName_current.setText(dcm.BeamSequence[0].TreatmentMachineName)
        except:
            self.lbl_TreatmentMachineName_current.setText('')

        try:
            self.lbl_StudyDescription_current.setText(dcm.StudyDescription)
        except:
            self.lbl_StudyDescription_current.setText('')

        try:
            self.lbl_SeriesDescription_current.setText(dcm.SeriesDescription)
        except:
            self.lbl_SeriesDescription_current.setText('')

        try:
            self.lbl_PatientName_current.setText(f'{dcm.PatientName.family_name}^{dcm.PatientName.given_name}')
        except:
            self.lbl_PatientName_current.setText('')

        try:
            self.lbl_PatientID_current.setText(dcm.PatientID)
        except:
            self.lbl_PatientID_current.setText('')

        try:
            self.lbl_PatientSex_current.setText(dcm.PatientSex)
        except:
            self.lbl_PatientSex_current.setText('')

        try:
            self.lbl_PatientBirthDate_current.setText(dcm.PatientBirthDate)
        except:
            self.lbl_PatientBirthDate_current.setText('')

    def fileopen(self):
        global dcm
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        open_file = filedialog.askopenfile()
        self.edit_fileopen.setText(open_file.name)
        dcm = pydicom.dcmread(open_file.name)
        self.reload_parameters_in_GUI(dcm)

    def folderopen(self):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        open_folder = filedialog.askdirectory()
        self.lbl_input_folder_path.setText(open_folder)
        #load in an RTPLAN if in folder - if not don't worry about it
        try:
            dcm = pydicom.dcmread(glob.glob(f'{self.lbl_input_folder_path.text()}/RTPLAN*.dcm')[0])
            self.reload_parameters_in_GUI(dcm)
        except:
            1+1

    def update_dcm(self):
        global dcm
        #updating the dcm
        if dcm.Modality in ['RTDOSE','RTPLAN','RTSTRUCT','CT','RTIMAGE']:
            if self.edit_StudyDescription.text():
                dcm.StudyDescription = self.edit_StudyDescription.text()
            if self.edit_SeriesDescription.text():
                dcm.SeriesDescription = self.edit_SeriesDescription.text()
            if self.edit_PatientName.text():
                dcm.PatientName = self.edit_PatientName.text()
            if self.edit_PatientID.text():
                dcm.PatientID = self.edit_PatientID.text()
            if self.edit_PatientSex.text():
                dcm.PatientSex = self.edit_PatientSex.text()
            if self.edit_PatientBirthDate.text():
                dcm.PatientBirthDate = self.edit_PatientBirthDate.text()
            if dcm.Modality in ['RTPLAN']:
                if self.edit_RTPlanLabel.text():
                    dcm.RTPlanLabel = self.edit_RTPlanLabel.text()
                if self.edit_RTPlanName.text():
                    dcm.RTPlanName = self.edit_RTPlanName.text()
                if self.edit_TreatmentMachineName.text():
                    for Beam in dcm.BeamSequence:
                        Beam.TreatmentMachineName = self.edit_TreatmentMachineName.text()

    #NEED TO SEE IF EMPTY AND IF EMPTY DONT DO IT
    def update_dcm_and_update_gui(self):
        global dcm
        self.update_dcm()
        #update the GUI
        self.reload_parameters_in_GUI(dcm)
        self.edit_StudyDescription.setText('')
        self.edit_SeriesDescription.setText('')
        self.edit_PatientName.setText('')
        self.edit_PatientID.setText('')
        self.edit_PatientSex.setText('')
        self.edit_PatientBirthDate.setText('')
        self.edit_RTPlanLabel.setText('')
        self.edit_RTPlanName.setText('')
        self.edit_TreatmentMachineName.setText('')

    def filesave(self):
        global dcm
        root = Tk()
        root.withdraw()
        root.attributes('-topmost',True)
        save_path = filedialog.asksaveasfile()
        dcm.save_as(save_path.name)

    def folderopen_output(self):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        open_folder = filedialog.askdirectory()
        self.lbl_outputs_folder_path.setText(open_folder)

    #read in the folder and start making the changes!
    def activate_folder(self):
        global dcm
        #read in the folder but only look at files that end with dcm
        i = 0
        dcmdir = [f for f in os.listdir(self.lbl_input_folder_path.text()) if f.endswith('.dcm')]
        for file in dcmdir:
            i += 1
            self.lbl_progress_folder.setText(f'{i}/{len(dcmdir)}')
            self.lbl_status_folder.setText(f'Modifying {file}')
            QApplication.processEvents()
            dcm = pydicom.dcmread(f'{self.lbl_input_folder_path.text()}/{file}')
            self.update_dcm()
            dcm.save_as(f'{self.lbl_outputs_folder_path.text()}/{file[:-4]}_updated.dcm')
        self.lbl_status_folder.setText('Completed')

    #Add in a button that reads in the folder and makes the changes but also creates a new set of SOPUID etc
    def activate_folder_new_UID(self):
        global dcm
        #read in the folder but only look at files that end with dcm
        # https://www.researchgate.net/figure/Relationships-between-various-UIDs-used-in-DICOM-RT-treatment-plans_fig1_264241699
        # Here we are assuming, RTPLAN, RTSTRUCT, RTDOSE, and CT
        # Loading all our new UIDs
        # For all DCM
        StudyInstanceUID = pydicom.uid.generate_uid()
        # For Image Series
        CT_SeriesInstanceUID = pydicom.uid.generate_uid()
        CT_FrameOfReferenceUID = pydicom.uid.generate_uid()
        # For Structure Series
        RTSTRUCT_SeriesInstanceUID = pydicom.uid.generate_uid()
        # For Plan Series
        RTPLAN_SeriesInstanceUID = pydicom.uid.generate_uid()
        # For Dose Series
        RTDOSE_SeriesInstanceUID = pydicom.uid.generate_uid()

        dcmdir = [f for f in os.listdir(self.lbl_input_folder_path.text()) if f.endswith('.dcm')]
        #Creating a dictionary of the new UIDs correponding to their old ones, so can update the old referenced dcms with the new ones.
        dcm_dict = {}
        for count,file in enumerate(dcmdir):
            self.lbl_progress_folder.setText(f'{count+1}/{len(dcmdir)}')
            self.lbl_status_folder.setText(f'Creating new UIDs from {file}')
            QApplication.processEvents()
            dcm = pydicom.dcmread(f'{self.lbl_input_folder_path.text()}/{file}')
            if dcm.Modality in ['CT']:
                dcm_dict[f'OLD_{dcm.Modality}_SOPInstanceUID_{dcm.SOPInstanceUID}'] = pydicom.uid.generate_uid()
            elif dcm.Modality in ['RTPLAN']:
                 dcm_dict[f'OLD_{dcm.Modality}_SOPInstanceUID_{dcm.SOPInstanceUID}'] = pydicom.uid.generate_uid()
            elif dcm.Modality in ['RTSTRUCT']:
                dcm_dict[f'OLD_{dcm.Modality}_SOPInstanceUID_{dcm.SOPInstanceUID}'] = pydicom.uid.generate_uid()
                for i,ReferencedFrameOfReference in enumerate(dcm.ReferencedFrameOfReferenceSequence):
                    # Updating FrameOfReferenceUID
                    dcm_dict[f'OLD_RTSTRUCT_FrameOfReferenceUID_{dcm.ReferencedFrameOfReferenceSequence[i].FrameOfReferenceUID}'] = pydicom.uid.generate_uid()
            elif dcm.Modality in ['RTDOSE']:
                dcm_dict[f'OLD_{dcm.Modality}_SOPInstanceUID_{dcm.SOPInstanceUID}'] = pydicom.uid.generate_uid()
            else:
                self.lbl_status_folder.setText(f'DCM with modality {dcm.Modality} not supported. Please remove {file} from folder before trying again')
                QApplication.processEvents()
                return

        #Now we reread the dcm and make the changes
        for count,file in enumerate(dcmdir):
            self.lbl_progress_folder.setText(f'{count+1}/{len(dcmdir)}')
            self.lbl_status_folder.setText(f'Applying new UIDs to {file}')
            QApplication.processEvents()
            dcm = pydicom.dcmread(f'{self.lbl_input_folder_path.text()}/{file}')

            #Updating study instance UID
            dcm.StudyInstanceUID = StudyInstanceUID

            #Updating CT DCM - This works fine if only CT DCM does not reference anything else
            if dcm.Modality in ['CT']:
                #updating Series Instance UID
                dcm.SeriesInstanceUID = CT_SeriesInstanceUID
                #Updating FrameOfReferenceUID
                dcm.FrameOfReferenceUID = CT_FrameOfReferenceUID
                # Updating SOPInstanceUID
                dcm.SOPInstanceUID = dcm_dict[f'OLD_{dcm.Modality}_SOPInstanceUID_{dcm.SOPInstanceUID}']
                #Replicating the metaheader data to be the same as above otherwise it breaks
                dcm.file_meta.MediaStorageSOPInstanceUID = dcm.SOPInstanceUID
            #Updating Structure Set - referencing CT
            elif dcm.Modality in ['RTSTRUCT']:
                dcm.SeriesInstanceUID = RTSTRUCT_SeriesInstanceUID
                # Updating SOPInstanceUID
                dcm.SOPInstanceUID = dcm_dict[f'OLD_{dcm.Modality}_SOPInstanceUID_{dcm.SOPInstanceUID}']
                #Replicating the metaheader data to be the same as above otherwise it breaks
                dcm.file_meta.MediaStorageSOPInstanceUID = dcm.SOPInstanceUID
                for i,ReferencedFrameOfReference in enumerate(dcm.ReferencedFrameOfReferenceSequence):
                    # Updating FrameOfReferenceUID with CT frame of reference
                    dcm.ReferencedFrameOfReferenceSequence[i].FrameOfReferenceUID = CT_FrameOfReferenceUID
                    for j,RTReferencedStudySequence in enumerate(ReferencedFrameOfReference.RTReferencedStudySequence):
                        #link this the study instance UID
                        dcm.ReferencedFrameOfReferenceSequence[i].RTReferencedStudySequence[j].ReferencedSOPInstanceUID = StudyInstanceUID
                        for k,RTReferencedSeriesSequence in enumerate(RTReferencedStudySequence.RTReferencedSeriesSequence):
                            #link this to ct image series UID
                            dcm.ReferencedFrameOfReferenceSequence[i].RTReferencedStudySequence[j].RTReferencedSeriesSequence[k].SeriesInstanceUID = CT_SeriesInstanceUID
                            for l,ContourImageSequence in enumerate(RTReferencedSeriesSequence.ContourImageSequence):
                                #link this to individ CT SOP UID
                                dcm.ReferencedFrameOfReferenceSequence[i].RTReferencedStudySequence[
                                    j].RTReferencedSeriesSequence[k].ContourImageSequence[l].ReferencedSOPInstanceUID = dcm_dict[f'OLD_CT_SOPInstanceUID_{dcm.ReferencedFrameOfReferenceSequence[i].RTReferencedStudySequence[j].RTReferencedSeriesSequence[k].ContourImageSequence[l].ReferencedSOPInstanceUID}']
            #Updating RTPLAN DCM - referencing CT and the structure set (what does it look like without structure set on export?)
            elif dcm.Modality in ['RTPLAN']:
                #Updating SeriesInstanceUID
                dcm.SeriesInstanceUID = RTPLAN_SeriesInstanceUID
                #Updating SOPInstanceUID
                dcm.SOPInstanceUID = dcm_dict[f'OLD_{dcm.Modality}_SOPInstanceUID_{dcm.SOPInstanceUID}']
                #Replicating the metaheader data to be the same as above otherwise it breaks
                dcm.file_meta.MediaStorageSOPInstanceUID = dcm.SOPInstanceUID
                #Updating Frame of ReferenceUID (same as Structure Series Frame of Refernce)
                dcm.FrameOfReferenceUID = CT_FrameOfReferenceUID
                #Now loop through referenced structures
                for i,RTPLAN_structure in enumerate(dcm.ReferencedStructureSetSequence):
                    #If this folder we are anonymising does not contain a structure set then create a random SOP instance UID to link to a phantom structure set
                    #updating the referenced SOP instance UID
                    try:
                        dcm.ReferencedStructureSetSequence[i].ReferencedSOPInstanceUID = dcm_dict[f'OLD_RTSTRUCT_SOPInstanceUID_{dcm.ReferencedStructureSetSequence[i].ReferencedSOPInstanceUID}']
                    except:
                        dcm.ReferencedStructureSetSequence[i].ReferencedSOPInstanceUID = pydicom.uid.generate_uid()
                for i,RTPLAN_dose in enumerate(dcm.DoseReferenceSequence):
                    #I don't think this links to anything so I am going to give it a random UID and hope it doesn't break
                    dcm.DoseReferenceSequence[i].DoseReferenceUID = pydicom.uid.generate_uid()
            #Updating DCM DOSE - looks at CT, struture and plan
            elif dcm.Modality in ['RTDOSE']:
                # Updating SeriesInstanceUID
                dcm.SeriesInstanceUID = RTDOSE_SeriesInstanceUID
                #updates Frame of Reference to CT image frame of reference - technically should be plan, but plan is updated to struct which is updated to CT. So will break if no CT file
                dcm.FrameOfReferenceUID = CT_FrameOfReferenceUID
                #Updating SOPInstanceUID
                dcm.SOPInstanceUID = dcm_dict[f'OLD_{dcm.Modality}_SOPInstanceUID_{dcm.SOPInstanceUID}']
                #Replicating the metaheader data to be the same as above otherwise it breaks
                dcm.file_meta.MediaStorageSOPInstanceUID = dcm.SOPInstanceUID
                #link to structure set - if no structure set in folder anon the uid
                try:
                    dcm.ReferencedStructureSetSequence[0].ReferencedSOPInstanceUID = dcm_dict[f'OLD_RTSTRUCT_SOPInstanceUID_{dcm.ReferencedStructureSetSequence[0].ReferencedSOPInstanceUID}']
                except:
                    dcm.ReferencedStructureSetSequence[0].ReferencedSOPInstanceUID = pydicom.uid.generate_uid()
                #link to RTPlan - if no rtplan in folder generate new uid
                try:
                    dcm.ReferencedRTPlanSequence[0].ReferencedSOPInstanceUID = dcm_dict[f'OLD_RTPLAN_SOPInstanceUID_{dcm.ReferencedRTPlanSequence[0].ReferencedSOPInstanceUID}']
                except:
                    dcm.ReferencedRTPlanSequence[0].ReferencedSOPInstanceUID = pydicom.uid.generate_uid()
            #Update plan name, patient name, ur etc
            self.update_dcm()
            dcm.save_as(f'{self.lbl_outputs_folder_path.text()}/{file[:-4]}.dcm')
        self.lbl_status_folder.setText('Completed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())








#rtplan_dcm = pydicom.dcmread(r'I:\Physics\_SRS Quality Assurance\01 Day of SRS QA - 11 Field Winston Lutz (10FFF)\SUN\_Day_of_SRS_RTplan.dcm')
#rtdose_dcm = pydicom.dcmread(r'I:\Physics\_SRS Quality Assurance\01 Day of SRS QA - 11 Field Winston Lutz (10FFF)\SUN\RTDOSE.1.2.246.352.71.7.724123028415.6569851.20200709162247.dcm')
#rtstruct_dcm = pydicom.dcmread(r'I:\Physics\_SRS Quality Assurance\01 Day of SRS QA - 11 Field Winston Lutz (10FFF)\SUN\RTSTRUCT.1.2.246.352.71.4.724123028415.540360.20200825153623.dcm')
#rtimage_dcm = pydicom.dcmread(r'I:\Physics\_SRS Quality Assurance\01 Day of SRS QA - 11 Field Winston Lutz (10FFF)\SUN\CT.1.2.246.352.62.1.5193994634324861573.3989485743527141040.dcm')



